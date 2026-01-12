
def start():
	print("Welcome to the Adventure Game!")
	ans = input("Start the game? (yes/no): ").strip().lower()
	if ans not in ("yes", "y"):
		print("You decided not to play. Goodbye.")
		return

	print("\nYou stand at the edge of a dark forest.")
	print("Choices:\n1) Enter the forest\n2) Walk away")
	choice = input("What do you do? (1/2 or text): ").strip().lower()

	enter_choices = {"1", "enter", "enter the forest", "enter forest"}
	walk_choices = {"2", "walk", "walk away", "leave"}

	if choice in enter_choices:
		print("\nYou step into the forest. The trees close behind you.")
		print("A narrow path splits ahead: left follows a faint stream, right heads toward a dark cave.")
		print("Choices:\n1) Follow the stream\n2) Head to the cave")
		second = input("Which way? (1/2 or text): ").strip().lower()

		stream_choices = {"1", "left", "stream", "follow the stream"}
		cave_choices = {"2", "right", "cave", "head to the cave", "enter cave"}

		if second in stream_choices:
			print("\nYou follow the stream and find a rickety bridge.")
			cross = input("Do you cross it? (yes/no): ").strip().lower()
			if cross in ("yes", "y"):
				print("You carefully cross and meet a kindly hermit who shares wisdom and reward. You win!")
			else:
				print("You decide not to risk it and return home safely, wondering what might have been.")
		elif second in cave_choices:
			print("\nYou enter the cave. Inside you spot a sleeping beast guarding a small chest.")
			action = input("Choices: sneak past or try to take the chest? (sneak/take): ").strip().lower()
			if action.startswith("sneak"):
				print("You sneak past successfully and take a single gem as a token. You escape — modest victory!")
			elif action.startswith("take"):
				print("The beast awakens and chases you out. You escape but drop your pack. Adventure over.")
			else:
				print("Hesitation wakes the beast; you flee empty-handed. Maybe next time.")
		else:
			print("\nConfused, you wander until dusk and then head home. The forest keeps its secrets.")
	elif choice in walk_choices:
		print("\nYou walk away safely, choosing a peaceful life of stories and memories. The adventure ends quietly.")
	else:
		print("\nUnable to decide, you sit by the forest edge until sunset and head home. Maybe next time!")


if __name__ == "__main__":
	start()

