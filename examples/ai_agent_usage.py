"""
Example demonstrating how an AI agent can use the Pixel Workbench Python API
to deterministically edit sprites and perform validations.
"""
from pixel_workbench import Workbench
from PIL import Image
import os

def setup_test_asset():
    # Setup test asset simulating 'warrior.png'
    img = Image.new("P", (16, 15))
    # Red body, transparent bg (0)
    img.putpalette([0, 0, 0, 255, 0, 0, 0, 0, 255] + [0]*759)
    img.info['transparency'] = 0

    # Paint body
    for y in range(8, 15):
        for x in range(4, 12):
            img.putpixel((x, y), 1)

    img.save("test_warrior.png")

def agent_workflow():
    setup_test_asset()
    print("Agent: Starting workflow on test_warrior.png")

    wb = Workbench()
    wb.open("test_warrior.png")

    # Check dimensions
    result = wb.validate()
    print(f"Agent: Initial validation ok? {result.ok}")

    # Agent wants to change the armor color from red (index 1) to blue (index 2)
    # The agent uses deterministic palette replacement.
    print("Agent: Replacing palette color...")
    wb.replace_color((255, 0, 0), (0, 0, 255))

    # Agent wants to add a badge (pixel edit)
    print("Agent: Adding a badge pixel...")
    wb.paint_index(8, 10, 2)

    # Agent validates after changes
    result = wb.validate()
    print(f"Agent: Post-edit validation ok? {result.ok}")

    # Save the modified asset
    wb.save("test_warrior_edited.png")
    print("Agent: Workflow complete. Saved as test_warrior_edited.png")

    # Cleanup
    os.remove("test_warrior.png")
    os.remove("test_warrior_edited.png")

if __name__ == "__main__":
    agent_workflow()
