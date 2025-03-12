"""
Main entry point for the Gradio-based CSV Question Answering and Visualization App.
"""

import gradio as gr
import pandas as pd
from modules.file_handler import load_csv
from modules.query_processor import process_query
from modules.visualization import generate_plot

# Global variable for the dataframe
df = None
def process_all(file_path, question, column_x, column_y):
    global df
    df, error = load_csv(file_path)
    if error:
        return "Error: " + error, None  # Return None instead of string

    answer = process_query(df, question)
    graph = generate_plot(df, column_x, column_y)

    return answer, graph  # Ensure graph is a Matplotlib figure


# Gradio UI Layout
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(" ## CSV Question Answering and Visualization Application", elem_id="title")

    with gr.Row():
        with gr.Column(scale=1, min_width=300):
            gr.Markdown("   Upload CSV File 📁 ")
            file_input = gr.File(label="Upload CSV File (size < 25mb)", type="filepath")

            gr.Markdown("    Ask a Question")
            query_input = gr.Textbox(label="Enter your query")

            gr.Markdown("Graph Inputs")
            x_col = gr.Textbox(label="Column X")
            y_col = gr.Textbox(label="Column Y")

            generate_button = gr.Button("Generate Response", elem_id="generate-btn")

        with gr.Column(scale=1):
            gr.Markdown(" AI Generated Response")
            query_output = gr.Textbox(label="Response", interactive=False)

            gr.Markdown("Graph ")
            plot_output = gr.Plot()

    # Button Action
    generate_button.click(process_all, inputs=[file_input, query_input, x_col, y_col], outputs=[query_output, plot_output])

demo.launch()
