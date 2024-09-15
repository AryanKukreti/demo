from utils.irrigation_utils import process_image_and_create_graph
from utils.gui_utils import get_image_path, onclick

def main():
    image_path = get_image_path()
    if image_path:
        print(f"Selected Starting Point: {onclick()}")

        # Process the image and create the graph
        G, points = process_image_and_create_graph(image_path)
        
        # You can add further logic for processing or visualizing the graph
        print("Graph has been created.")

if __name__ == "__main__":
    main()
