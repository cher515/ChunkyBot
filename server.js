const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: "sk-None-Fvuh08Am230o3ErIDPshT3BlbkFJK3Ageov6yRtrosfpvrVg",
});
const openai = new OpenAIApi(configuration);

async function chatWithGpt(prompt) {
  const response = await openai.createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: prompt },
    ],
  });
  return response.data.choices[0].message.content.trim();
}

async function main() {
  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });

  while (true) {
    const userInput = await new Promise(resolve => {
      readline.question('You: ', resolve);
    });

    if (['quit', 'exit', 'bye'].includes(userInput.toLowerCase())) {
      break;
    }

    try {
      const response = await chatWithGpt(userInput);
      console.log("ChunkyBot: ", response);
    } catch (error) {
      console.error("An error occurred:", error);
    }
  }

  readline.close();
}

main();