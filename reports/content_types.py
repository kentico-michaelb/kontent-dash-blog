import plotly.express as px

def build_types_chart(client):
    type_response = client.get_content_types()
    item_response = client.get_content_items()

    types = {}

    # add Kontent type counts to a dictionary
    for content_type in type_response.types:
        types[content_type.codename] = 0

    # increment content type count per item of respective type
    for item in item_response.items:
        types[item.content_type] += 1 

    data = {"content types":types.keys(), "count": types.values()}

    fig = px.bar(data, x="content types", y="count")

    return fig