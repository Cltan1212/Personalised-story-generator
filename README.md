
# Project Title

This project is a Story Generator application designed to help users create short stories and their corresponding cover images. It's particularly aimed at adults aged 20-30 who enjoy reading short stories. The application takes user prompts, generates a short story, and then creates a cover image based on the story's theme. It leverages the power of OpenAI's GPT-3.5-turbo for story generation and DALL-E 2 for image generation.


## Badges

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Replit](https://img.shields.io/badge/Replit-DD1200?style=for-the-badge&logo=Replit&logoColor=white)


## Features

### 1. User-Friendly Interface:
- Easy-to-use form where users can input keywords to generate stories.
- Interactive and responsive design using Streamlit, providing a seamless user experience.

### 2. AI-Powered Story Generation:
- Utilizes OpenAI's GPT-3.5-turbo model to generate engaging and creative 100-word short stories.
- Stories are tailored for adults aged 20-30, ensuring relevant and captivating content.
  
### 3. Dynamic Cover Image Creation:
- Employs OpenAI's DALL-E 2 model to generate a detailed image prompt based on the generated story.
- Creates visually appealing cover images that match the theme of the story, enhancing the reading experience.

### 4. Seamless Integration:
- Smooth integration between story generation and image creation processes.
- Automatically generates and displays the cover image upon story creation.

### 5. Real-Time Feedback:
- Provides real-time feedback and updates using Streamlit's spinner and success messages.
- Ensures users are informed of the progress and completion of story and image generation.

### 6. Session State Management:
- Maintains the state of user inputs and outputs across interactions without refreshing the entire page.
- Enhances the user experience by preserving the conversation history.
  
### 7. Scalable and Extendable:
- Designed to easily incorporate additional features, such as audio narration of the stories.
- Flexible structure allows for future enhancements and integration with other AI models.

### 8. Secure API Usage:
- Utilizes OpenAI API securely with API key management.
- Ensures secure and reliable interaction with the AI models.


## Usage/Example:

### User Input:
User enters the following keywords: "mysterious forest adventure".

### Story Generation:
The AI generates a short story based on the user's keywords:
```
In the heart of the mysterious forest, Alex stumbled upon an ancient, hidden path. The trees whispered secrets of forgotten adventures, and the air was thick with magic. As the sun dipped below the horizon, a soft glow revealed a hidden village. Here, creatures of legend roamed freely, and time itself seemed to dance to an ancient tune. Alex knew this was the beginning of an extraordinary adventure, one that would change their life forever. The forest held many secrets, and Alex was determined to uncover them all.
```

### Cover Image Design:
Based on the story, the AI creates a detailed image prompt for the cover:
```
A glowing path in a dark, enchanted forest leading to a hidden village, with mystical creatures.
```

### Image Generation:
The AI generates the cover image based on the design prompt and displays it to the user.

