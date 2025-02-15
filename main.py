#load
def load():
    pass

#feature
def feature(): 
    pass

#boxplot
def boxplot():
    pass #testonly
  
#annotations
    def annotations():
        pass

#featvanno
    def featvanno():
        pass
        # 5. FEAT. VS ANNO. (Heatmap) ----------------------------
        ui.nav_panel("Feat. Vs Anno.",
            ui.card({"style": "width:100%;"},
                ui.column(12,
                    ui.row(
                        ui.column(2,
                            ui.input_select("hm1_anno", "Select an Annotation", choices=[]),
                            ui.input_select("hm1_layer", "Select a Table", choices=[]),
                            ui.input_select("hm1_cmap", "Select Color Map", choices=["viridis", "plasma", "inferno", "magma", "cividis","coolwarm", "RdYlBu", "Spectral", "PiYG", "PRGn"]),  # Dropdown for color maps
                            ui.input_slider("hm_x_label_rotation", "Rotate X Axis Labels", min=0, max=90, value=25),
                            ui.input_checkbox("dendogram", "Include Dendrogram", False),
                            ui.div(id="main-hm1_check"),
                            ui.div(id="main-hm2_check"),
                            ui.div(id="main-min_num"),
                            ui.div(id="main-max_num"),
                            ui.input_action_button("go_hm1", "Render Plot", class_="btn-success"),
                            ui.div(
                                    {"style": "padding-top: 20px;"},
                                    ui.output_ui("download_button_ui")
                                )
                        ),
                        ui.column(10,
                            ui.div(
                                    {"style": "padding-bottom: 100px;"},
                            ui.output_plot("spac_Heatmap", width="100%", height="100vh")
                            )
                        )
                    )
                )
            )
        ),

#annovanno

#spatial

#umap

#scatterplot
