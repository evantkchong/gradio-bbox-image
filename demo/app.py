
import gradio as gr
from gradio_bbox_image import BBoxImage


example = BBoxImage().example_inputs()

demo = gr.Interface(
    lambda x:x,
    BBoxImage(),  # interactive version of your component
    BBoxImage(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


demo.launch()
