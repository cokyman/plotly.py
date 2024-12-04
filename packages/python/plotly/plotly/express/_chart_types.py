from typing import Any, Dict, Literal, List
from warnings import warn
from narwhals.stable.v1.typing import IntoDataFrame, IntoSeries

from ._core import make_figure
from ._doc import make_docstring
import plotly.graph_objs as go

_wide_mode_xy_append = [
    "Either `x` or `y` can optionally be a list of column references or array_likes, ",
    "in which case the data will be treated as if it were 'wide' rather than 'long'.",
]
_cartesian_append_dict = dict(x=_wide_mode_xy_append, y=_wide_mode_xy_append)


def scatter(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    size: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    text: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    error_x: IntoSeries | str | int | None = None,
    error_x_minus: IntoSeries | str | int | None = None,
    error_y: IntoSeries | str | None = None,
    error_y_minus: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    orientation: Literal["v", "h"] | None = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: List[float] | None = None,
    color_continuous_midpoint: float | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    opacity: float | None = None,
    size_max: int | None = None,
    marginal_x: Literal["histogram", "rug", "box", "violin"] | None = None,
    marginal_y: Literal["histogram", "rug", "box", "violin"] | None = None,
    trendline: Literal["ols", "lowess", "rolling", "ewm", "expanding"] | None = None,
    trendline_options: Dict[str, Any] | None = None,
    trendline_color_override: str | None = None,
    trendline_scope: Literal["trace", "overall"] = "trace",
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    render_mode: Literal["auto", "svg", "webgl"] = "auto",
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a scatter plot, each row of `data_frame` is represented by a symbol
    mark in 2D space.
    """
    return make_figure(args=locals(), constructor=go.Scatter)


scatter.__doc__ = make_docstring(scatter, append_dict=_cartesian_append_dict)


def density_contour(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    z: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    orientation: Literal["v", "h"] | None = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    marginal_x: Literal["histogram", "rug", "box", "violin"] | None = None,
    marginal_y: Literal["histogram", "rug", "box", "violin"] | None = None,
    trendline: Literal["ols", "lowess", "rolling", "ewm", "expanding"] | None = None,
    trendline_options: Dict[str, Any] | None = None,
    trendline_color_override: str | None = None,
    trendline_scope: Literal["trace", "overall"] = "trace",
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    histfunc: Literal["count", "sum", "avg", "min", "max"] | None = None,
    histnorm: Literal["percent", "probability", "density"] | None = None,
    nbinsx: IntoSeries | str | int | None = None,
    nbinsy: IntoSeries | str | int | None = None,
    text_auto: bool | str = False,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a density contour plot, rows of `data_frame` are grouped together
    into contour marks to visualize the 2D distribution of an aggregate
    function `histfunc` (e.g. the count or sum) of the value `z`.
    """
    return make_figure(
        args=locals(),
        constructor=go.Histogram2dContour,
        trace_patch=dict(
            contours=dict(coloring="none"),
            histfunc=histfunc,
            histnorm=histnorm,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            xbingroup="x",
            ybingroup="y",
        ),
    )


density_contour.__doc__ = make_docstring(
    density_contour,
    append_dict=dict(
        x=_wide_mode_xy_append,
        y=_wide_mode_xy_append,
        z=[
            "For `density_heatmap` and `density_contour` these values are used as the inputs to `histfunc`.",
        ],
        histfunc=["The arguments to this function are the values of `z`."],
    ),
)


def density_heatmap(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    z: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    orientation: Literal["v", "h"] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    marginal_x: Literal["histogram", "rug", "box", "violin"] | None = None,
    marginal_y: Literal["histogram", "rug", "box", "violin"] | None = None,
    opacity: float | None = None,
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    histfunc: Literal["count", "sum", "avg", "min", "max"] | None = None,
    histnorm: Literal["percent", "probability", "density"] | None = None,
    nbinsx: IntoSeries | str | int | None = None,
    nbinsy: IntoSeries | str | int | None = None,
    text_auto: bool | str = False,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a density heatmap, rows of `data_frame` are grouped together into
    colored rectangular tiles to visualize the 2D distribution of an
    aggregate function `histfunc` (e.g. the count or sum) of the value `z`.
    """
    return make_figure(
        args=locals(),
        constructor=go.Histogram2d,
        trace_patch=dict(
            histfunc=histfunc,
            histnorm=histnorm,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            xbingroup="x",
            ybingroup="y",
        ),
    )


density_heatmap.__doc__ = make_docstring(
    density_heatmap,
    append_dict=dict(
        x=_wide_mode_xy_append,
        y=_wide_mode_xy_append,
        z=[
            "For `density_heatmap` and `density_contour` these values are used as the inputs to `histfunc`.",
        ],
        histfunc=[
            "The arguments to this function are the values of `z`.",
        ],
    ),
)


def line(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    line_group: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    line_dash: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    text: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    error_x: IntoSeries | str | int | None = None,
    error_x_minus: IntoSeries | str | int | None = None,
    error_y: IntoSeries | str | int | None = None,
    error_y_minus: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    orientation: Literal["v", "h"] | None = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    line_dash_sequence: List[str] | None = None,
    line_dash_map: Dict[str, str] | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    markers: bool = False,
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    line_shape: Literal["linear", "spline", "hv", "vh", "hvh", "vhv"] | None = None,
    render_mode: Literal["auto", "svg", "webgl"] = "auto",
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a 2D line plot, each row of `data_frame` is represented as a vertex of
    a polyline mark in 2D space.
    """
    return make_figure(args=locals(), constructor=go.Scatter)


line.__doc__ = make_docstring(line, append_dict=_cartesian_append_dict)


def area(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    line_group: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    pattern_shape: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    text: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    pattern_shape_sequence: List[str] | None = None,
    pattern_shape_map: Dict[str, str] | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    markers: bool = False,
    orientation: Literal["v", "h"] | None = None,
    groupnorm: Literal["fraction", "percent"] | None = None,
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    line_shape: Literal["linear", "spline", "hv", "vh", "hvh", "vhv"] | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a stacked area plot, each row of `data_frame` is represented as
    a vertex of a polyline mark in 2D space. The area between
    successive polylines is filled.
    """
    return make_figure(
        args=locals(),
        constructor=go.Scatter,
        trace_patch=dict(stackgroup=1, mode="lines", groupnorm=groupnorm),
    )


area.__doc__ = make_docstring(area, append_dict=_cartesian_append_dict)


def bar(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    pattern_shape: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    text: IntoSeries | str | int | None = None,
    base: IntoSeries | str | int | None = None,
    error_x: IntoSeries | str | int | None = None,
    error_x_minus: IntoSeries | str | int | None = None,
    error_y: IntoSeries | str | int | None = None,
    error_y_minus: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    pattern_shape_sequence: List[str] | None = None,
    pattern_shape_map: Dict[str, str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    opacity: float | None = None,
    orientation: Literal["v", "h"] | None = None,
    barmode: Literal["group", "overlay", "relative"] = "relative",
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    text_auto: bool | str = False,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a bar plot, each row of `data_frame` is represented as a rectangular
    mark.
    """
    return make_figure(
        args=locals(),
        constructor=go.Bar,
        trace_patch=dict(textposition="auto"),
        layout_patch=dict(barmode=barmode),
    )


bar.__doc__ = make_docstring(bar, append_dict=_cartesian_append_dict)


def timeline(
    data_frame: IntoDataFrame | None = None,
    x_start: IntoSeries | str | int | None = None,
    x_end: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    pattern_shape: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    text: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    pattern_shape_sequence: List[str] | None = None,
    pattern_shape_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    opacity: float | None = None,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a timeline plot, each row of `data_frame` is represented as a rectangular
    mark on an x axis of type `date`, spanning from `x_start` to `x_end`.
    """
    return make_figure(
        args=locals(),
        constructor="timeline",
        trace_patch=dict(textposition="auto", orientation="h"),
        layout_patch=dict(barmode="overlay"),
    )


timeline.__doc__ = make_docstring(timeline)


def histogram(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    pattern_shape: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    pattern_shape_sequence: List[str] | None = None,
    pattern_shape_map: Dict[str, str] | None = None,
    marginal: Literal["histogram", "rug", "box", "violin"] | None = None,
    opacity: float | None = None,
    orientation: Literal["v", "h"] | None = None,
    barmode: Literal["group", "overlay", "relative"] = "relative",
    barnorm: Literal["fraction", "percent"] | None = None,
    histnorm: Literal["percent", "probability", "density"] | None = None,
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    histfunc: Literal["count", "sum", "avg", "min", "max"] | None = None,
    cumulative: bool | None = None,
    nbins: int | None = None,
    text_auto: bool | str = False,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a histogram, rows of `data_frame` are grouped together into a
    rectangular mark to visualize the 1D distribution of an aggregate
    function `histfunc` (e.g. the count or sum) of the value `y` (or `x` if
    `orientation` is `'h'`).
    """
    return make_figure(
        args=locals(),
        constructor=go.Histogram,
        trace_patch=dict(
            histnorm=histnorm,
            histfunc=histfunc,
            cumulative=dict(enabled=cumulative),
        ),
        layout_patch=dict(barmode=barmode, barnorm=barnorm),
    )


histogram.__doc__ = make_docstring(
    histogram,
    append_dict=dict(
        x=["If `orientation` is `'h'`, these values are used as inputs to `histfunc`."]
        + _wide_mode_xy_append,
        y=["If `orientation` is `'v'`, these values are used as inputs to `histfunc`."]
        + _wide_mode_xy_append,
        histfunc=[
            "The arguments to this function are the values of `y` (`x`) if `orientation` is `'v'` (`'h'`).",
        ],
    ),
)


def ecdf(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    line_dash: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    markers: bool = False,
    lines: bool = True,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    line_dash_sequence: List[str] | None = None,
    line_dash_map: Dict[str, str] | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    marginal: Literal["histogram", "rug", "box", "violin"] | None = None,
    opacity: float | None = None,
    orientation: Literal["v", "h"] | None = None,
    ecdfnorm="probability",
    ecdfmode="standard",
    render_mode: Literal["auto", "svg", "webgl"] = "auto",
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a Empirical Cumulative Distribution Function (ECDF) plot, rows of `data_frame`
    are sorted by the value `x` (or `y` if `orientation` is `'h'`) and their cumulative
    count (or the cumulative sum of `y` if supplied and `orientation` is `h`) is drawn
    as a line.
    """
    return make_figure(args=locals(), constructor=go.Scatter)


ecdf.__doc__ = make_docstring(
    ecdf,
    append_dict=dict(
        x=[
            "If `orientation` is `'h'`, the cumulative sum of this argument is plotted rather than the cumulative count."
        ]
        + _wide_mode_xy_append,
        y=[
            "If `orientation` is `'v'`, the cumulative sum of this argument is plotted rather than the cumulative count."
        ]
        + _wide_mode_xy_append,
    ),
)


def violin(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    orientation: Literal["v", "h"] | None = None,
    violinmode: Literal["group", "overlay"] | None = None,
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    points: Literal["outliers", "suspectedoutliers", "all"] | bool | None = None,
    box: bool = False,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a violin plot, rows of `data_frame` are grouped together into a
    curved mark to visualize their distribution.
    """
    return make_figure(
        args=locals(),
        constructor=go.Violin,
        trace_patch=dict(
            points=points,
            box=dict(visible=box),
            scalegroup=True,
            x0=" ",
            y0=" ",
        ),
        layout_patch=dict(violinmode=violinmode),
    )


violin.__doc__ = make_docstring(violin, append_dict=_cartesian_append_dict)


def box(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    orientation: Literal["v", "h"] | None = None,
    boxmode: Literal["group", "overlay"] | None = None,
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    points: Literal["outliers", "suspectedoutliers", "all"] | bool | None = None,
    notched: bool = False,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a box plot, rows of `data_frame` are grouped together into a
    box-and-whisker mark to visualize their distribution.

    Each box spans from quartile 1 (Q1) to quartile 3 (Q3). The second
    quartile (Q2) is marked by a line inside the box. By default, the
    whiskers correspond to the box' edges +/- 1.5 times the interquartile
    range (IQR: Q3-Q1), see "points" for other options.
    """
    return make_figure(
        args=locals(),
        constructor=go.Box,
        trace_patch=dict(boxpoints=points, notched=notched, x0=" ", y0=" "),
        layout_patch=dict(boxmode=boxmode),
    )


box.__doc__ = make_docstring(box, append_dict=_cartesian_append_dict)


def strip(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    orientation: Literal["v", "h"] | None = None,
    stripmode: Literal["group", "overlay"] | None = None,
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a strip plot each row of `data_frame` is represented as a jittered
    mark within categories.
    """
    return make_figure(
        args=locals(),
        constructor=go.Box,
        trace_patch=dict(
            boxpoints="all",
            pointpos=0,
            hoveron="points",
            fillcolor="rgba(255,255,255,0)",
            line={"color": "rgba(255,255,255,0)"},
            x0=" ",
            y0=" ",
        ),
        layout_patch=dict(boxmode=stripmode),
    )


strip.__doc__ = make_docstring(strip, append_dict=_cartesian_append_dict)


def scatter_3d(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    z: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    size: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    error_x: IntoSeries | str | int | None = None,
    error_x_minus: IntoSeries | str | int | None = None,
    error_y: IntoSeries | str | int | None = None,
    error_y_minus: IntoSeries | str | int | None = None,
    error_z: IntoSeries | str | int | None = None,
    error_z_minus: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    size_max: int | None = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    opacity: float | None = None,
    log_x: bool = False,
    log_y: bool = False,
    log_z: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    range_z: IntoSeries | str | int | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a 3D scatter plot, each row of `data_frame` is represented by a
    symbol mark in 3D space.
    """
    return make_figure(args=locals(), constructor=go.Scatter3d)


scatter_3d.__doc__ = make_docstring(scatter_3d)


def line_3d(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    z: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    line_dash: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    line_group: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    error_x: IntoSeries | str | int | None = None,
    error_x_minus: IntoSeries | str | int | None = None,
    error_y: IntoSeries | str | int | None = None,
    error_y_minus: IntoSeries | str | int | None = None,
    error_z: IntoSeries | str | int | None = None,
    error_z_minus: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    line_dash_sequence: List[str] | None = None,
    line_dash_map: Dict[str, str] | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    markers: bool = False,
    log_x: bool = False,
    log_y: bool = False,
    log_z: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    range_z: IntoSeries | str | int | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a 3D line plot, each row of `data_frame` is represented as a vertex of
    a polyline mark in 3D space.
    """
    return make_figure(args=locals(), constructor=go.Scatter3d)


line_3d.__doc__ = make_docstring(line_3d)


def scatter_ternary(
    data_frame: IntoDataFrame | None = None,
    a: IntoSeries | str | int | None = None,
    b: IntoSeries | str | int | None = None,
    c: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    size: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    opacity: float | None = None,
    size_max: int | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a ternary scatter plot, each row of `data_frame` is represented by a
    symbol mark in ternary coordinates.
    """
    return make_figure(args=locals(), constructor=go.Scatterternary)


scatter_ternary.__doc__ = make_docstring(scatter_ternary)


def line_ternary(
    data_frame: IntoDataFrame | None = None,
    a: IntoSeries | str | int | None = None,
    b: IntoSeries | str | int | None = None,
    c: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    line_dash: IntoSeries | str | int | None = None,
    line_group: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    text: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    line_dash_sequence: List[str] | None = None,
    line_dash_map: Dict[str, str] | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    markers: bool = False,
    line_shape: Literal["linear", "spline", "hv", "vh", "hvh", "vhv"] | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a ternary line plot, each row of `data_frame` is represented as
    a vertex of a polyline mark in ternary coordinates.
    """
    return make_figure(args=locals(), constructor=go.Scatterternary)


line_ternary.__doc__ = make_docstring(line_ternary)


def scatter_polar(
    data_frame: IntoDataFrame | None = None,
    r: IntoSeries | str | int | None = None,
    theta: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    size: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    text: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    opacity: float | None = None,
    direction="clockwise",
    start_angle: int = 90,
    size_max: int | None = None,
    range_r: List[float] | None = None,
    range_theta: List[float] | None = None,
    log_r: bool = False,
    render_mode: Literal["auto", "svg", "webgl"] = "auto",
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a polar scatter plot, each row of `data_frame` is represented by a
    symbol mark in polar coordinates.
    """
    return make_figure(args=locals(), constructor=go.Scatterpolar)


scatter_polar.__doc__ = make_docstring(scatter_polar)


def line_polar(
    data_frame: IntoDataFrame | None = None,
    r: IntoSeries | str | int | None = None,
    theta: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    line_dash: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    line_group: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    line_dash_sequence: List[str] | None = None,
    line_dash_map: Dict[str, str] | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    markers: bool = False,
    direction="clockwise",
    start_angle: int = 90,
    line_close: bool = False,
    line_shape: Literal["linear", "spline", "hv", "vh", "hvh", "vhv"] | None = None,
    render_mode: Literal["auto", "svg", "webgl"] = "auto",
    range_r: List[float] | None = None,
    range_theta: List[float] | None = None,
    log_r: bool = False,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a polar line plot, each row of `data_frame` is represented as a
    vertex of a polyline mark in polar coordinates.
    """
    return make_figure(args=locals(), constructor=go.Scatterpolar)


line_polar.__doc__ = make_docstring(line_polar)


def bar_polar(
    data_frame: IntoDataFrame | None = None,
    r: IntoSeries | str | int | None = None,
    theta: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    pattern_shape: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    base: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    pattern_shape_sequence: List[str] | None = None,
    pattern_shape_map: Dict[str, str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    barnorm: Literal["fraction", "percent"] | None = None,
    barmode: Literal["group", "overlay", "relative"] = "relative",
    direction="clockwise",
    start_angle: int = 90,
    range_r: List[float] | None = None,
    range_theta: List[float] | None = None,
    log_r: bool = False,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a polar bar plot, each row of `data_frame` is represented as a wedge
    mark in polar coordinates.
    """
    return make_figure(
        args=locals(),
        constructor=go.Barpolar,
        layout_patch=dict(barnorm=barnorm, barmode=barmode),
    )


bar_polar.__doc__ = make_docstring(bar_polar)


def choropleth(
    data_frame: IntoDataFrame | None = None,
    lat: IntoSeries | str | int | None = None,
    lon: IntoSeries | str | int | None = None,
    locations: IntoSeries | str | int | None = None,
    locationmode: str | None = None,
    geojson: Dict | None = None,
    featureidkey: str | None = None,
    color: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    projection: (
        Literal[
            "equirectangular",
            "mercator",
            "orthographic",
            "natural earth",
            "kavrayskiy7",
            "miller",
            "robinson",
            "eckert4",
            "azimuthal equal area",
            "azimuthal equidistant",
            "conic equal area",
            "conic conformal",
            "conic equidistant",
            "gnomonic",
            "stereographic",
            "mollweide",
            "hammer",
            "transverse mercator",
            "albers usa",
            "winkel tripel",
            "aitoff",
            "sinusoidal",
        ]
        | None
    ) = None,
    scope: (
        Literal[
            "world", "usa", "europe", "asia", "africa", "north america", "south america"
        ]
        | None
    ) = None,
    center: Dict[str, float] | None = None,
    fitbounds: Literal[False, "locations", "geojson"] | None = None,
    basemap_visible: bool | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a choropleth map, each row of `data_frame` is represented by a
    colored region mark on a map.
    """
    return make_figure(
        args=locals(),
        constructor=go.Choropleth,
        trace_patch=dict(locationmode=locationmode),
    )


choropleth.__doc__ = make_docstring(choropleth)


def scatter_geo(
    data_frame: IntoDataFrame | None = None,
    lat: IntoSeries | str | int | None = None,
    lon: IntoSeries | str | int | None = None,
    locations: IntoSeries | str | int | None = None,
    locationmode: str | None = None,
    geojson: Dict | None = None,
    featureidkey: str | None = None,
    color: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    size: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    opacity: float | None = None,
    size_max: int | None = None,
    projection: (
        Literal[
            "equirectangular",
            "mercator",
            "orthographic",
            "natural earth",
            "kavrayskiy7",
            "miller",
            "robinson",
            "eckert4",
            "azimuthal equal area",
            "azimuthal equidistant",
            "conic equal area",
            "conic conformal",
            "conic equidistant",
            "gnomonic",
            "stereographic",
            "mollweide",
            "hammer",
            "transverse mercator",
            "albers usa",
            "winkel tripel",
            "aitoff",
            "sinusoidal",
        ]
        | None
    ) = None,
    scope: (
        Literal[
            "world", "usa", "europe", "asia", "africa", "north america", "south america"
        ]
        | None
    ) = None,
    center: Dict[str, float] | None = None,
    fitbounds: Literal[False, "locations", "geojson"] | None = None,
    basemap_visible: bool | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a geographic scatter plot, each row of `data_frame` is represented
    by a symbol mark on a map.
    """
    return make_figure(
        args=locals(),
        constructor=go.Scattergeo,
        trace_patch=dict(locationmode=locationmode),
    )


scatter_geo.__doc__ = make_docstring(scatter_geo)


def line_geo(
    data_frame: IntoDataFrame | None = None,
    lat: IntoSeries | str | int | None = None,
    lon: IntoSeries | str | int | None = None,
    locations: IntoSeries | str | int | None = None,
    locationmode: str | None = None,
    geojson: Dict | None = None,
    featureidkey: str | None = None,
    color: IntoSeries | str | int | None = None,
    line_dash: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    line_group: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    line_dash_sequence: List[str] | None = None,
    line_dash_map: Dict[str, str] | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    markers: bool = False,
    projection: (
        Literal[
            "equirectangular",
            "mercator",
            "orthographic",
            "natural earth",
            "kavrayskiy7",
            "miller",
            "robinson",
            "eckert4",
            "azimuthal equal area",
            "azimuthal equidistant",
            "conic equal area",
            "conic conformal",
            "conic equidistant",
            "gnomonic",
            "stereographic",
            "mollweide",
            "hammer",
            "transverse mercator",
            "albers usa",
            "winkel tripel",
            "aitoff",
            "sinusoidal",
        ]
        | None
    ) = None,
    scope: (
        Literal[
            "world", "usa", "europe", "asia", "africa", "north america", "south america"
        ]
        | None
    ) = None,
    center: Dict[str, float] | None = None,
    fitbounds: Literal[False, "locations", "geojson"] | None = None,
    basemap_visible: bool | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a geographic line plot, each row of `data_frame` is represented as
    a vertex of a polyline mark on a map.
    """
    return make_figure(
        args=locals(),
        constructor=go.Scattergeo,
        trace_patch=dict(locationmode=locationmode),
    )


line_geo.__doc__ = make_docstring(line_geo)


def scatter_map(
    data_frame: IntoDataFrame | None = None,
    lat: IntoSeries | str | int | None = None,
    lon: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    size: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    opacity: float | None = None,
    size_max: int | None = None,
    zoom: int = 8,
    center: Dict[str, float] | None = None,
    map_style: (
        Literal[
            "basic",
            "carto-darkmatter",
            "carto-darkmatter-nolabels",
            "carto-positron",
            "carto-positron-nolabels",
            "carto-voyager",
            "carto-voyager-nolabels",
            "dark",
            "light",
            "open-street-map",
            "outdoors",
            "satellite",
            "satellite-streets",
            "streets",
            "white-bg",
        ]
        | None
    ) = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a scatter map, each row of `data_frame` is represented by a
    symbol mark on the map.
    """
    return make_figure(args=locals(), constructor=go.Scattermap)


scatter_map.__doc__ = make_docstring(scatter_map)


def choropleth_map(
    data_frame: IntoDataFrame | None = None,
    geojson: Dict | None = None,
    featureidkey: str | None = None,
    locations: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    opacity: float | None = None,
    zoom: int = 8,
    center: Dict[str, float] | None = None,
    map_style: (
        Literal[
            "basic",
            "carto-darkmatter",
            "carto-darkmatter-nolabels",
            "carto-positron",
            "carto-positron-nolabels",
            "carto-voyager",
            "carto-voyager-nolabels",
            "dark",
            "light",
            "open-street-map",
            "outdoors",
            "satellite",
            "satellite-streets",
            "streets",
            "white-bg",
        ]
        | None
    ) = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a choropleth map, each row of `data_frame` is represented by a
    colored region on the map.
    """
    return make_figure(args=locals(), constructor=go.Choroplethmap)


choropleth_map.__doc__ = make_docstring(choropleth_map)


def density_map(
    data_frame: IntoDataFrame | None = None,
    lat: IntoSeries | str | int | None = None,
    lon: IntoSeries | str | int | None = None,
    z: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    opacity: float | None = None,
    zoom: int = 8,
    center: Dict[str, float] | None = None,
    map_style: (
        Literal[
            "basic",
            "carto-darkmatter",
            "carto-darkmatter-nolabels",
            "carto-positron",
            "carto-positron-nolabels",
            "carto-voyager",
            "carto-voyager-nolabels",
            "dark",
            "light",
            "open-street-map",
            "outdoors",
            "satellite",
            "satellite-streets",
            "streets",
            "white-bg",
        ]
        | None
    ) = None,
    radius: int | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a density map, each row of `data_frame` contributes to the intensity of
    the color of the region around the corresponding point on the map.
    """
    return make_figure(
        args=locals(), constructor=go.Densitymap, trace_patch=dict(radius=radius)
    )


density_map.__doc__ = make_docstring(density_map)


def line_map(
    data_frame: IntoDataFrame | None = None,
    lat: IntoSeries | str | int | None = None,
    lon: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    line_group: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    zoom: int = 8,
    center: Dict[str, float] | None = None,
    map_style: (
        Literal[
            "basic",
            "carto-darkmatter",
            "carto-darkmatter-nolabels",
            "carto-positron",
            "carto-positron-nolabels",
            "carto-voyager",
            "carto-voyager-nolabels",
            "dark",
            "light",
            "open-street-map",
            "outdoors",
            "satellite",
            "satellite-streets",
            "streets",
            "white-bg",
        ]
        | None
    ) = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a line map, each row of `data_frame` is represented as
    a vertex of a polyline mark on the map.
    """
    return make_figure(args=locals(), constructor=go.Scattermap)


line_map.__doc__ = make_docstring(line_map)


def scatter_mapbox(
    data_frame: IntoDataFrame | None = None,
    lat: IntoSeries | str | int | None = None,
    lon: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    size: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    opacity: float | None = None,
    size_max: int | None = None,
    zoom: int = 8,
    center: Dict[str, float] | None = None,
    mapbox_style: str | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    *scatter_mapbox* is deprecated! Use *scatter_map* instead.
    Learn more at: https://plotly.com/python/mapbox-to-maplibre/
    In a Mapbox scatter plot, each row of `data_frame` is represented by a
    symbol mark on a Mapbox map.
    """
    warn(
        "*scatter_mapbox* is deprecated!"
        + " Use *scatter_map* instead."
        + " Learn more at: https://plotly.com/python/mapbox-to-maplibre/",
        stacklevel=2,
        category=DeprecationWarning,
    )
    return make_figure(args=locals(), constructor=go.Scattermapbox)


scatter_mapbox.__doc__ = make_docstring(scatter_mapbox)


def choropleth_mapbox(
    data_frame: IntoDataFrame | None = None,
    geojson: Dict | None = None,
    featureidkey: str | None = None,
    locations: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    opacity: float | None = None,
    zoom: int = 8,
    center: Dict[str, float] | None = None,
    mapbox_style: str | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    *choropleth_mapbox* is deprecated! Use *choropleth_map* instead.
    Learn more at: https://plotly.com/python/mapbox-to-maplibre/
    In a Mapbox choropleth map, each row of `data_frame` is represented by a
    colored region on a Mapbox map.
    """
    warn(
        "*choropleth_mapbox* is deprecated!"
        + " Use *choropleth_map* instead."
        + " Learn more at: https://plotly.com/python/mapbox-to-maplibre/",
        stacklevel=2,
        category=DeprecationWarning,
    )
    return make_figure(args=locals(), constructor=go.Choroplethmapbox)


choropleth_mapbox.__doc__ = make_docstring(choropleth_mapbox)


def density_mapbox(
    data_frame: IntoDataFrame | None = None,
    lat: IntoSeries | str | int | None = None,
    lon: IntoSeries | str | int | None = None,
    z: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    opacity: float | None = None,
    zoom: int = 8,
    center: Dict[str, float] | None = None,
    mapbox_style: str | None = None,
    radius: int | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    *density_mapbox* is deprecated! Use *density_map* instead.
    Learn more at: https://plotly.com/python/mapbox-to-maplibre/
    In a Mapbox density map, each row of `data_frame` contributes to the intensity of
    the color of the region around the corresponding point on the map
    """
    warn(
        "*density_mapbox* is deprecated!"
        + " Use *density_map* instead."
        + " Learn more at: https://plotly.com/python/mapbox-to-maplibre/",
        stacklevel=2,
        category=DeprecationWarning,
    )
    return make_figure(
        args=locals(), constructor=go.Densitymapbox, trace_patch=dict(radius=radius)
    )


density_mapbox.__doc__ = make_docstring(density_mapbox)


def line_mapbox(
    data_frame: IntoDataFrame | None = None,
    lat: IntoSeries | str | int | None = None,
    lon: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    text: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    line_group: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    zoom: int = 8,
    center: Dict[str, float] | None = None,
    mapbox_style: str | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    *line_mapbox* is deprecated! Use *line_map* instead.
    Learn more at: https://plotly.com/python/mapbox-to-maplibre/
    In a Mapbox line plot, each row of `data_frame` is represented as
    a vertex of a polyline mark on a Mapbox map.
    """
    warn(
        "*line_mapbox* is deprecated!"
        + " Use *line_map* instead."
        + " Learn more at: https://plotly.com/python/mapbox-to-maplibre/",
        stacklevel=2,
        category=DeprecationWarning,
    )
    return make_figure(args=locals(), constructor=go.Scattermapbox)


line_mapbox.__doc__ = make_docstring(line_mapbox)


def scatter_matrix(
    data_frame: IntoDataFrame | None = None,
    dimensions: IntoSeries | List[str] | List[int] | None = None,
    color: IntoSeries | str | int | None = None,
    symbol: IntoSeries | str | int | None = None,
    size: IntoSeries | str | int | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    symbol_sequence: List[str] | None = None,
    symbol_map: Dict[str, str] | None = None,
    opacity: float | None = None,
    size_max: int | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a scatter plot matrix (or SPLOM), each row of `data_frame` is
    represented by a multiple symbol marks, one in each cell of a grid of
    2D scatter plots, which plot each pair of `dimensions` against each
    other.
    """
    return make_figure(
        args=locals(), constructor=go.Splom, layout_patch=dict(dragmode="select")
    )


scatter_matrix.__doc__ = make_docstring(scatter_matrix)


def parallel_coordinates(
    data_frame: IntoDataFrame | None = None,
    dimensions: IntoSeries | List[str] | List[int] | None = None,
    color: IntoSeries | str | int | None = None,
    labels: Dict[str, str] = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a parallel coordinates plot, each row of `data_frame` is represented
    by a polyline mark which traverses a set of parallel axes, one for each
    of the `dimensions`.
    """
    return make_figure(args=locals(), constructor=go.Parcoords)


parallel_coordinates.__doc__ = make_docstring(parallel_coordinates)


def parallel_categories(
    data_frame: IntoDataFrame | None = None,
    dimensions: IntoSeries | List[str] | List[int] | None = None,
    color: IntoSeries | str | int | None = None,
    labels: Dict[str, str] = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
    dimensions_max_cardinality: int = 50,
) -> go.Figure:
    """
    In a parallel categories (or parallel sets) plot, each row of
    `data_frame` is grouped with other rows that share the same values of
    `dimensions` and then plotted as a polyline mark through a set of
    parallel axes, one for each of the `dimensions`.
    """
    return make_figure(args=locals(), constructor=go.Parcats)


parallel_categories.__doc__ = make_docstring(parallel_categories)


def pie(
    data_frame: IntoDataFrame | None = None,
    names: IntoSeries | str | int | None = None,
    values: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
    opacity: float | None = None,
    hole: float | None = None,
) -> go.Figure:
    """
    In a pie plot, each row of `data_frame` is represented as a sector of a
    pie.
    """
    if color_discrete_sequence is not None:
        layout_patch = {"piecolorway": color_discrete_sequence}
    else:
        layout_patch = {}
    return make_figure(
        args=locals(),
        constructor=go.Pie,
        trace_patch=dict(showlegend=(names is not None), hole=hole),
        layout_patch=layout_patch,
    )


pie.__doc__ = make_docstring(
    pie,
    override_dict=dict(
        hole=[
            "float",
            "Sets the fraction of the radius to cut out of the pie."
            "Use this to make a donut chart.",
        ],
    ),
)


def sunburst(
    data_frame: IntoDataFrame | None = None,
    names: IntoSeries | str | int | None = None,
    values: IntoSeries | str | int | None = None,
    parents: IntoSeries | str | int | None = None,
    path: IntoSeries | List[str] | List[int] | None = None,
    ids: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    labels: Dict[str, str] = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
    branchvalues: Literal["total", "remainder"] | None = None,
    maxdepth: int | None = None,
) -> go.Figure:
    """
    A sunburst plot represents hierarchial data as sectors laid out over
    several levels of concentric rings.
    """
    if color_discrete_sequence is not None:
        layout_patch = {"sunburstcolorway": color_discrete_sequence}
    else:
        layout_patch = {}
    if path is not None and (ids is not None or parents is not None):
        raise ValueError(
            "Either `path` should be provided, or `ids` and `parents`."
            "These parameters are mutually exclusive and cannot be passed together."
        )
    if path is not None and branchvalues is None:
        branchvalues = "total"
    return make_figure(
        args=locals(),
        constructor=go.Sunburst,
        trace_patch=dict(branchvalues=branchvalues, maxdepth=maxdepth),
        layout_patch=layout_patch,
    )


sunburst.__doc__ = make_docstring(sunburst)


def treemap(
    data_frame: IntoDataFrame | None = None,
    names: IntoSeries | str | int | None = None,
    values: IntoSeries | str | int | None = None,
    parents: IntoSeries | str | int | None = None,
    ids: IntoSeries | str | int | None = None,
    path: IntoSeries | List[str] | List[int] | None = None,
    color: IntoSeries | str | int | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    labels: Dict[str, str] = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
    branchvalues: Literal["total", "remainder"] | None = None,
    maxdepth: int | None = None,
) -> go.Figure:
    """
    A treemap plot represents hierarchial data as nested rectangular
    sectors.
    """
    if color_discrete_sequence is not None:
        layout_patch = {"treemapcolorway": color_discrete_sequence}
    else:
        layout_patch = {}
    if path is not None and (ids is not None or parents is not None):
        raise ValueError(
            "Either `path` should be provided, or `ids` and `parents`."
            "These parameters are mutually exclusive and cannot be passed together."
        )
    if path is not None and branchvalues is None:
        branchvalues = "total"
    return make_figure(
        args=locals(),
        constructor=go.Treemap,
        trace_patch=dict(branchvalues=branchvalues, maxdepth=maxdepth),
        layout_patch=layout_patch,
    )


treemap.__doc__ = make_docstring(treemap)


def icicle(
    data_frame: IntoDataFrame | None = None,
    names: IntoSeries | str | int | None = None,
    values: IntoSeries | str | int | None = None,
    parents: IntoSeries | str | int | None = None,
    path: IntoSeries | List[str] | List[int] | None = None,
    ids: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    color_continuous_scale: List[str] | None = None,
    range_color: IntoSeries | str | int | None = None,
    color_continuous_midpoint: float | None = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    labels: Dict[str, str] = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
    branchvalues: Literal["total", "remainder"] | None = None,
    maxdepth: int | None = None,
) -> go.Figure:
    """
    An icicle plot represents hierarchial data with adjoined rectangular
    sectors that all cascade from root down to leaf in one direction.
    """
    if color_discrete_sequence is not None:
        layout_patch = {"iciclecolorway": color_discrete_sequence}
    else:
        layout_patch = {}
    if path is not None and (ids is not None or parents is not None):
        raise ValueError(
            "Either `path` should be provided, or `ids` and `parents`."
            "These parameters are mutually exclusive and cannot be passed together."
        )
    if path is not None and branchvalues is None:
        branchvalues = "total"
    return make_figure(
        args=locals(),
        constructor=go.Icicle,
        trace_patch=dict(branchvalues=branchvalues, maxdepth=maxdepth),
        layout_patch=layout_patch,
    )


icicle.__doc__ = make_docstring(icicle)


def funnel(
    data_frame: IntoDataFrame | None = None,
    x: IntoSeries | str | int | None = None,
    y: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    facet_row: IntoSeries | str | int | None = None,
    facet_col: IntoSeries | str | int | None = None,
    facet_col_wrap: int = 0,
    facet_row_spacing: float | None = None,
    facet_col_spacing: float | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    text: IntoSeries | str | int | None = None,
    animation_frame: IntoSeries | str | int | None = None,
    animation_group: IntoSeries | str | int | None = None,
    category_orders: Dict[str, List[str]] | None = None,
    labels: Dict[str, str] = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    opacity: float | None = None,
    orientation: Literal["v", "h"] | None = None,
    log_x: bool = False,
    log_y: bool = False,
    range_x: List[float] | None = None,
    range_y: List[float] | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
) -> go.Figure:
    """
    In a funnel plot, each row of `data_frame` is represented as a
    rectangular sector of a funnel.
    """
    return make_figure(args=locals(), constructor=go.Funnel)


funnel.__doc__ = make_docstring(funnel, append_dict=_cartesian_append_dict)


def funnel_area(
    data_frame: IntoDataFrame | None = None,
    names: IntoSeries | str | int | None = None,
    values: IntoSeries | str | int | None = None,
    color: IntoSeries | str | int | None = None,
    color_discrete_sequence: List[str] | None = None,
    color_discrete_map: Dict[str, str] | None = None,
    hover_name: IntoSeries | str | int | None = None,
    hover_data: IntoSeries | str | List[str] | int | None = None,
    custom_data: IntoSeries | str | List[str] | int | None = None,
    labels: Dict[str, str] = None,
    title: str | None = None,
    subtitle: str | None = None,
    template: (
        Literal[
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]
        | None
    ) = None,
    width: int | None = None,
    height: int | None = None,
    opacity: float | None = None,
) -> go.Figure:
    """
    In a funnel area plot, each row of `data_frame` is represented as a
    trapezoidal sector of a funnel.
    """
    if color_discrete_sequence is not None:
        layout_patch = {"funnelareacolorway": color_discrete_sequence}
    else:
        layout_patch = {}
    return make_figure(
        args=locals(),
        constructor=go.Funnelarea,
        trace_patch=dict(showlegend=(names is not None)),
        layout_patch=layout_patch,
    )


funnel_area.__doc__ = make_docstring(funnel_area)
