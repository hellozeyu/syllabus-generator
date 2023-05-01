from shiny import App, render, reactive, ui
from docxtpl import DocxTemplate
from docx2pdf import convert
from pathlib import Path
import shinyswatch


app_ui = ui.page_navbar(

    shinyswatch.theme.superhero(),

    ui.nav(
        'Navbar 1',
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.tags.h2('Course Info'),
                ui.tags.hr(),
                ui.input_text("program_name", "Program Name", placeholder="M.S. in Enterprise Risk Management"),
                ui.input_text("course_name", "Course Name", placeholder="Applied Coding for Risk Management"),
                ui.input_text("schedule", "Course Schedule", placeholder="Mondays at 6:10pm on Campus"),
                ui.input_text("number_of_credits", "Number of Credits", placeholder="3"),
                ui.input_text("elective", "Elective", placeholder="Elective"),

                ui.tags.h2('Instructors'),
                ui.tags.hr(),
                ui.input_text("instructor", "Instructor", placeholder="David Romoff"),
                ui.input_text("instructor_oh", "Office Hours", placeholder="TBD"),
                ui.input_text("instructor_rp", "Response Policy", placeholder="Emails replied to within 2 hours during business hours."),

                ui.tags.h2('Teaching Assistant'),
                ui.tags.hr(),
                ui.input_text("ta", "Teaching Assistant", placeholder="TBD"),
                ui.input_text("ta_oh", "Office Hours", placeholder="TBD"),
                ui.input_text("ta_rp", "Response Policy", placeholder="Emails replied to within 2 hours during business hours."),

                ui.tags.h2('Course Details'),
                ui.tags.hr(),
                ui.input_text_area("course_overview", "Course Overview", placeholder="Enter text"),

                ui.input_text_area("learning_objectives", "Learning Objectives", placeholder="Enter text"),

                ui.input_text_area("readings", "Readings", placeholder="Enter text"),

                ui.input_text_area("assignments", "Assignments and Assessments", placeholder="Enter text"),
                ui.row(
                    ui.p(ui.input_action_button("generate", "Generate", class_="btn-primary")),
                    # ui.output_text_verbatim("txt"),
                ),
                width=3
            ),
            ui.panel_main(
                ui.navset_tab(
                    ui.nav(
                        "Preview",
                        ui.output_ui(id='preview'))
                )
            ),
        ),
    ),
    title="Syllabus Generator"
)


def server(input, output, session):
    @output
    @render.text
    @reactive.event(input.generate)
    def preview():
        print('Clicked')
        doc = DocxTemplate("templates/syllabus_template.docx")

        context = {'program_name': input.program_name(),
                   'course_name': input.course_name(),
                   'schedule': input.schedule(),
                   'number_of_credits': input.number_of_credits(),
                   'elective': input.elective(),
                   'instructor': input.instructor(),
                   'instructor_oh': input.instructor_oh(),
                   'ta': input.ta(),
                   'ta_oh': input.ta_oh(),
                   'ta_rp': input.ta_rp(),
                   'course_overview': input.course_overview(),
                   'learning_objectives': input.learning_objectives(),
                   'readings': input.readings(),
                   'assignments': input.assignments()}

        doc.render(context)
        doc.save("generated_syllabus.docx")
        convert("generated_syllabus.docx", "www/generated_syllabus.pdf")

        return '<iframe style="height:1000px; width:100%" src="generated_syllabus.pdf"></iframe>'


www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)

