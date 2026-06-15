from google import genai
import inquirer
import os, sys

os.system('cls' if os.name == 'nt' else 'clear')

def ascii_logo():
	print("...\./.../-\.|--.|\./|.|--.|--.|\.|.---.|--.........")
	print("....X....|._.|--.|.|.|.|--.|--.|.\|..|..|--.........")
	print(".../.\...\_/.|__.|.|.|.|__.|__.|..\..|..|__.........")
	print("....................................................")
	print("...\./....^..._-..---.|--.|-\.|-\...^...|\./|.......")
	print("....X..../_\..|_...|..|--.|-/.|.|../_\..|.|.|.......")
	print(".../.\../...\.._|..|..|__.|.\.|-/./...\.|.|.|.......")
	print("....................................................")
	print("...\./..............................................")
	print("....X...............................................")
	print(".../.\..............................................")

ascii_logo()

def ai_selecter():
	questions = [inquirer.List(
		name="ai-model",
		message="select your model",
		choices=['Gemini', 'Copilot', 'ChatGPT', 'Claude'],
		carousel=True,
	)]
	anwser = inquirer.prompt(questions)

	if confirm_choice() == False:
		os.system('cls' if os.name == 'nt' else 'clear')
		ai_selecter()
		return

	match anwser['ai-model']:
		case "Gemini":
			print("Gemini starting...")
			#setup_gemini()
		case "Copilot":
			print("Copilot starting...")
			#setup_copilot()
		case "ChatGPT":
			print("ChatGPT starting...")
			#setup_chatgpt()
		case "Claude":
			print("Claude starting...")
			#setup_claude()

def confirm_choice():
	print("Are you sure (Y/n):", end=" ")
	yn = input()
	if yn == "Y":
		return True
	elif yn == "n":
		return False
	else:
		print("choose Yes or no")
		return confirm_choice()

ai_selecter()
