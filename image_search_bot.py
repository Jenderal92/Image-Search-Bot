import os
import requests
import sys

def print_banner():
    banner = """
    ###############################################
    #                                             #
    #          IMAGE SEARCH BOT             #
    #      Powered by Google Custom Search API    #
    #                                             #
    ###############################################
    """
    print(banner)

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def search_and_download_images(api_key, cse_id, query, num_images, output_folder):
    print("\n[INFO] Starting image search for query: '{}'".format(query))
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'cx': cse_id,
        'key': api_key,
        'searchType': 'image',
        'num': 10, 
    }

    downloaded = 0
    start = 1

    create_folder(output_folder)

    while downloaded < num_images:
        params['start'] = start
        try:
            response = requests.get(url, params=params)
            data = response.json()

            if 'items' not in data:
                print("[ERROR] No items found in the response!")
                break

            for item in data['items']:
                if downloaded >= num_images:
                    break

                try:
                    image_url = item['link']
                    print("[INFO] Downloading image: {}".format(image_url))

                    image_data = requests.get(image_url).content
                    filename = os.path.join(output_folder, "image_{}.jpg".format(downloaded + 1))
                    
                    with open(filename, 'wb') as f:
                        f.write(image_data)

                    print("[SUCCESS] Saved: {}".format(filename))
                    downloaded += 1
                except Exception as e:
                    print("[ERROR] Failed to download image: {}".format(e))
            
            start += 10
        except Exception as e:
            print("[ERROR] API request failed: {}".format(e))
            break

    print("\n[INFO] Downloaded {} images to folder '{}'".format(downloaded, output_folder))

if __name__ == "__main__":
    print_banner()
    
    api_key = "YOUR_GOOGLE_API_KEY"
    cse_id = "YOUR_CUSTOM_SEARCH_ENGINE_ID"

    query = raw_input("[INPUT] Enter search keyword: ")
    num_images = int(raw_input("[INPUT] Number of images to download: "))
    output_folder = "downloaded_images"

    search_and_download_images(api_key, cse_id, query, num_images, output_folder)
