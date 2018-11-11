from colour import Color
from django.shortcuts import render

from benchmarks.models import CandidateModel

colors = list(Color('red').range_to(Color('green'), 100))
color_suffix = '_color'

ceilings = {
    'v4': .892,
    'it': .817,
    'behavior': .479,
    'imagenet_top1': 100,
}


def view(request):
    models = CandidateModel.objects.order_by('-brain_score')
    data = {}
    for field in ['brain_score', 'V4', 'IT', 'behavior', 'imagenet_top1']:
        ceiling = ceilings[field] if field in ceilings else None
        values = [getattr(model, field) for model in models]
        min_value, max_value = min(values), max(values)
        data[field] = represent(max_value)
        normalized_max = normalize(max_value, 0, max_value=ceiling)
        min_normalized_max = normalize(max_value, min_value, max_value=ceiling)
        data[field + color_suffix] = representative_color(min_normalized_max, alpha_max=normalized_max)

        for model in models:
            value = getattr(model, field)
            setattr(model, field, represent(value))

            if field == 'brain_score':
                rank = values.index(value)
                setattr(model, 'rank', rank + 1)

            normalized_value = normalize(value, min_value, max_value=ceiling)
            color = representative_color(normalized_value, alpha_max=normalized_max)
            setattr(model, field + color_suffix, color)
    context = {'models': models, 'data': data}
    return render(request, 'benchmarks/index.html', context)


def normalize(value, min_value, max_value=None):
    max_value = max_value or (1 if value < 1 else 100)
    return (value - min_value) / (max_value - min_value)


def represent(value):
    return "{:.3f}".format(value).lstrip('0') if value < 1 else "{:.1f}".format(value)


def representative_color(value, alpha_max=100):
    if value < 1:
        value *= 100
        if alpha_max < 1:
            alpha_max *= 100
    step = int(value)
    color = colors[step]
    color = tuple(c * 255 for c in color.rgb)
    fallback_color = tuple(round(c) for c in color)
    color += (value / alpha_max,)
    return f"background-color: rgb{fallback_color}; background-color: rgba{color};"
