# H2E: Transforming Hindi Hits Into English Epics

### Abstract

Dubbing movies into different languages presents significant challenges in maintaining the emotional nuances and authenticity of the original dialogue. Current methods often result in either human-dependent dubbing, which can be time-consuming and costly, or robotic dubbing lacking emotional depth and synchronization with background music. This project introduces an innovative audio dubbing approach that seamlessly integrates background music and speaker expressions into dubbed audio.

### Key Features

- **Seamless Integration:** The proposed model seamlessly integrates background music and speaker expressions into the dubbed audio, ensuring a cohesive viewing experience.
- **Advanced Techniques:** Leveraging a denoiser to distinguish background music and noise, and a state-of-the-art speech-extraction model, the model accurately extracts vocals and expressions from the video file.
- **Text-to-Speech Synthesis:** The final step involves infusing the background music and speaker expressions with the voice generated by a text-to-speech model, resulting in high-quality dubbed audio.
- **Empirical Evidence:** To validate the effectiveness of the proposed approach, a benchmark dataset of movies for Hindi-to-English dubbing is introduced, providing comprehensive empirical evidence.

![Problem Statement](/images/problem_statement.png)

Given a Hindi movie video, our model dubs the movie into English with the same expression and background music.

### Repository Contents

- **Code:** Contains the implementation of the proposed audio dubbing model, including denoising algorithms, speech-extraction models, and text-to-speech synthesis.
- **Data:** Includes the benchmark dataset of movies for Hindi-to-English dubbing, facilitating reproducibility and further research.
- **Documentation:** Provides detailed instructions for running the code, training the model, and evaluating performance.
- **Results:** Presents the empirical results obtained from testing the model on the benchmark dataset, along with comparisons to the state-of-the-art.

### How to Use

1. Clone the repository to your local machine.
2. Install the necessary dependencies as listed in the documentation.
3. Preprocess the dataset and train the audio dubbing model according to the provided instructions.
4. Evaluate the model's performance using the benchmark dataset and compare it with existing methods.
5. Explore opportunities for further improvements and contributions.

### Contributors

- [Gouthami Reddy Godhala, Samriddha Sanyal, and Vijayasree Asam]

