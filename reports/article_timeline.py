from kontent_delivery.builders.filter_builder import Filter
import pandas as pd
import plotly.express as px

def build_post_timeline(client):
    item_response = client.get_content_items(
        Filter("system.type", "[eq]", "article")
    )

    chart_items = []
    chart_post_date = []

    for item in item_response.items:
        chart_items.append(item.name)
        chart_post_date.append(item.elements.post_date.value)

    df = pd.DataFrame(dict(item=chart_items, post_date=chart_post_date))

    # # Use column names of df for the different parameters x, y, color, ...
    fig = px.scatter(df, x="post_date", y="item",
                    title="Article post timeline",
                    labels={"Post Date":"Date item posted"} # customize axis label
                    )

    return fig