from kontent_delivery.builders.filter_builder import Filter
import plotly.express as px

def build_personas_pie(client):
    item_response = client.get_content_items(
        Filter("system.type", "[eq]", "article")
    )

    personas_response = client.get_taxonomy("personas")
    chart_personas = {}

    # identify personas to be counted
    def get_taxonomy_terms(terms):
        for persona in terms:
            chart_personas[persona.name] = 0
            if persona.terms:
                get_taxonomy_terms(persona.terms)
        

    get_taxonomy_terms(personas_response.terms)

    # increment persona count per item
    for item in item_response.items:
        for persona in item.elements.personas.value:
            chart_personas[persona.name] += 1 

    data = {"personas":chart_personas.keys(), "count": chart_personas.values()}

    fig = px.pie(data, names="personas", values="count",
                title='Assigned article personas')
    return fig