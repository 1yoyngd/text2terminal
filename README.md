# Natural Language to Terminal Command Translator
This tool translates natural language instructions into terminal commands, currently tailored for macOS users.

## Setup Instructions
The setup process described below is for the Zsh shell. The steps can be adapted for Bash if needed.

### Accessing the `.zshrc` File
1. Open your terminal.
2. Open the `.zshrc` file, you can use either `nano` or `vim`:

   For `nano`, enter:
   ```
   nano ~/.zshrc
   ```

   For `vim`, enter:
   ```
   vim ~/.zshrc
   ```
3. Type the following function to the end of `zshrc` file:
   ```
   function q() {
    source /path/to/your/venv/bin/activate
    python /path/to/your/project/main.py "$@"
    deactivate
   }
   ```
   You can replace `"q"` with any other keyword you want to use to call the translator. Save the updated file.
4. Source your saved file:
    ```
    source ~/.zshrc
    ```
6. Give the access to your script using:
   ```
   chmod +x /path/to/your/project/main.py
   ```
7. Set your `OPENAI_API_KEY` variable in .env file in the same folder where your project is.
8. Now any time typing `q "your question"` - the python script will be pulled.


## Examples
1. q "List all the files on my Desktop"
2. q "Remove nested directories"
3. q "Force Quitting Apps"
