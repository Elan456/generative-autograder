import os
import yaml
import gradio as gr
from pathlib import Path

def save_project_config(
    project_id,
    directions_pdf,   # single-file dict or None
    sample_outputs,   # list of dicts or None
    sample_code,      # list of dicts or None
    other_uploads,    # list of dicts or None
    config_option
):
    """
    Save the provided configuration and uploaded files to
    project_configs/<project_id>/.
    """

    # return str([type(project_id), type(directions_pdf), type(sample_outputs), type(sample_code), type(other_uploads), type(config_option)])

    if not project_id:
        return "Error: project_id must not be empty."
    
    return os.getcwd()

    # 1. Create the project's folder if it doesn't exist
    project_folder = Path("src/project_configs") / project_id
    project_folder.mkdir(parents=True, exist_ok=True)

    # 2. Prepare config data to save in config.yaml
    config_data = {
        "project_id": project_id,
        "config_option": config_option,
    }
    config_yaml_path = project_folder / "config.yaml"

    # Write config.yaml
    with open(config_yaml_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(config_data, f)

    # 3. Save directions PDF if provided
    if directions_pdf is not None:  # directions_pdf is a dict
        # Typically: directions_pdf["data"] = bytes, directions_pdf["orig_name"] or ["name"] = filename
        pdf_data = open(directions_pdf, "rb").read()
        pdf_name = directions_pdf.split("/")[-1]  # Extract filename from path
        pdf_path = project_folder / pdf_name
        with open(pdf_path, "wb") as f:
            f.write(pdf_data)

    # 4. Save sample output files if provided
    if sample_outputs is not None:
        for output_file in sample_outputs:
            out_data = open(output_file, "rb").read()
            out_name = output_file.split("/")[-1]  # Extract filename from path
            out_path = project_folder / out_name
            with open(out_path, "wb") as f:
                f.write(out_data)

    # 5. Save sample code files if provided
    if sample_code is not None:
        for code_file in sample_code:
            code_data = open(code_file, "rb").read()
            code_name = code_file.split("/")[-1]
            code_path = project_folder / code_name
            with open(code_path, "wb") as f:
                f.write(code_data)

    # 6. Save any other uploaded files
    if other_uploads is not None:
        for other_file in other_uploads:
            other_data = open(other_file, "rb").read()
            other_name = other_file.split("/")[-1]
            other_path = project_folder / other_name
            with open(other_path, "wb") as f:
                f.write(other_data)

    return f"Config for project '{project_id}' saved successfully in {project_folder}."


def create_config_interface():
    """
    Create and return a Gradio Blocks interface for project configuration with nicer layout.
    """
    with gr.Blocks() as config_app:
        gr.Markdown(
            """
            <h1 style="text-align:center; margin-bottom: 10px;">
                Auto-Hinter Configuration
            </h1>
            <p style="text-align:center;">
                Configure your project ID, directions, sample outputs, and more below.
            </p>
            <hr/>
            """,
        )

        with gr.Row():
            with gr.Column():
                project_id = gr.Textbox(
                    label="Project ID",
                    placeholder="e.g. cpsc101-proj1",
                    info="A unique identifier for the project."
                )
                config_option = gr.Radio(
                    choices=["Option A", "Option B", "Option C"],
                    label="Configuration Option",
                    value="Option A",
                    info="Select a configuration mode."
                )

            # We can keep the "Save Config" button in its own column or row:
            with gr.Column():
                save_button = gr.Button("Save Config", variant="primary")

        # Let's put all file uploads in a separate row so they line up nicely
        with gr.Blocks() as upload_section:
            gr.Markdown("### Uploads")
            with gr.Row():
                directions_pdf = gr.File(
                    label="Directions PDF",
                    file_types=[".pdf"],
                    # info="Upload the project instructions in PDF format."
                )
                sample_outputs = gr.Files(
                    label="Sample Outputs (.txt)",
                    file_types=[".txt"],
                    # info="Upload one or more text files containing sample outputs."
                )
            with gr.Row():
                sample_code = gr.Files(
                    label="Sample Code (.py, .cpp, etc.)",
                    file_types=[".py", ".java", ".cpp", ".c", ".txt"],
                    # info="Upload code examples for the project."
                )
                other_uploads = gr.Files(
                    label="Other Relevant Files",
                    # info="Any additional resources you want to include."
                )

        output_message = gr.Markdown()

        # Link button click to the save function
        save_button.click(
            fn=save_project_config,
            inputs=[project_id, directions_pdf, sample_outputs, sample_code, other_uploads, config_option],
            outputs=output_message
        )

    return config_app

# For standalone testing, uncomment:
if __name__ == "__main__":
    create_config_interface().launch(server_name="0.0.0.0", server_port=7860)
