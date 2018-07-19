import _plotly_utils.basevalidators


class ArrangementValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='arrangement', parent_name='sankey', **kwargs
    ):
        super(ArrangementValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            values=['snap', 'perpendicular', 'freeform', 'fixed'],
            **kwargs
        )