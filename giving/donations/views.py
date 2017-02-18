from collections import defaultdict, OrderedDict
import datetime

from django.shortcuts import render

from .models import Amount

def index(request):
    amounts = Amount.objects.all()

    grouped = {}
    for a in amounts:
        d = a.donation_date
        key = tuple(d.isocalendar()[:2])
        grouped.setdefault(key, []).append(a)

    weekly_totals = {}
    for g in grouped:
        weekly_totals[g] = 0
        for a in grouped[g]:
            weekly_totals[g] += a.amount

    d = defaultdict(list)
    for a, b in grouped.items() + weekly_totals.items():
        d[a].append(b)
    d = dict(d)
    od = OrderedDict(sorted(d.items(), reverse=True))

    context = {
        'weeks': grouped,
        'totals': od
    }

    return render(request, 'donations/index.html', context)
