🌧️ Chainlit Weather Agent ☀️
A simple yet powerful chatbot that provides real-time weather information via a web interface. It is built using Chainlit for the UI and an agentic system powered by LiteLLM and the OpenAI Agents SDK.

✨ Features
Interactive Chat Interface: A clean, web-based UI for interacting with the agent.

Natural Language Queries: Ask for the weather in any location using plain English.

Real-time Weather Data: Uses a real weather API as a tool to fetch up-to-the-minute data.

Flexible LLM Integration: Leverages LiteLLM to support a wide array of LLM providers.

Extensible Agent Architecture: The agent's logic is orchestrated by the OpenAI Agents SDK, making it easy to add more tools and functionality.

⚙️ Installation
First, clone this repository and navigate into the project directory.

git clone https://github.com/your-username/chainlit-weather-agent.git
cd chainlit-weather-agent

🛠️ Under the Hood
This project is a great example of building an LLM-powered chatbot using a few key technologies.

Chainlit
Chainlit provides the beautiful, interactive front-end for the chatbot. It handles the message history, user input, and displaying the agent's responses. All of this is accomplished with minimal code, allowing you to focus on the agent's logic.

LiteLLM
LiteLLM is an abstraction layer that allows the agent to communicate with various LLM providers using a single, consistent API. This means you can easily switch from OpenAI to another provider like Anthropic or Gemini by simply changing the model name and API key, without modifying the agent's core logic.

OpenAI Agents SDK
The agent's "brain" is built with the OpenAI Agents SDK. This framework allows you to define a set of instructions for the LLM and provide it with "tools"—in this case, a function to get weather data. The LLM intelligently decides when to use the get_weather tool and what arguments to pass to it based on the user's query.

Real Weather API as a Tool
The agent's ability to fetch and use real-time data is the core of its functionality. A simple Python function calls the OpenWeatherMap API, and the OpenAI Agents SDK exposes this function to the LLM. The LLM's prompt is configured to understand the purpose of this tool, enabling it to provide accurate, up-to-date weather information.