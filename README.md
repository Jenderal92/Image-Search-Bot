#Image Search Bot

**Image Search Bot** is a Python 2.7-based tool designed to automatically search for images using the Google Custom Search JSON API. This tool enables users to search for and download images based on specific keywords. It is particularly useful for saving time and effort in gathering images from the internet.

---

#### **2. How to Use**  
To use **Image Search Bot**, follow these steps:

1. **Obtain API Key and Search Engine ID**  
   - Visit the **Google Developers Console** and create a project.  
   - Enable the **Custom Search API**.  
   - Obtain the **API Key** and create a **Custom Search Engine ID (CSE ID)**.

2. **Install Dependencies**  
   Ensure you have Python 2.7 installed. Download the `requests` library by running:  
   ```bash
   pip install requests
   ```

3. **Configure the Tool**  
   - Open the Python script file.  
   - Enter your API Key and CSE ID in the `api_key` and `cse_id` variables.

4. **Run the Tool**  
   - Execute the script via the terminal using the command:  
     ```bash
     python image_search_bot.py
     ```
   - Input your search keywords and specify the number of images you want to download.

5. **Search Results**  
   - The tool will save the images in the `downloaded_images` folder or a folder location of your choice.

---

#### **3. Tool Features**  
1. **Automated Keyword-Based Search**  
   - The tool searches for images based on the keywords you input.

2. **Image Downloading**  
   - Images from the search results are automatically downloaded to a local folder.

3. **Easy Configuration**  
   - Users only need to input their API Key and Search Engine ID once.

4. **Supports Multi-Download**  
   - Download up to 100 images in one search, subject to API limits.

---

#### **4. Tool Functions**  
- **Simplifies Image Collection**  
  Helps users quickly gather images without manual internet searches.

- **Time Efficiency**  
  By simply entering a keyword, the tool automatically downloads relevant images.

- **Wide Applications**  
  Suitable for research, projects, presentations, or building image collections.

- **Customizable**  
  Users can adjust the number of images downloaded, storage location, or integrate the tool into larger pipelines.

---
