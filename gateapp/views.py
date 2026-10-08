from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Visitor
from .forms import VisitorForm


def dashboard(request):

    total_visitors = Visitor.objects.count()

    inside_visitors = Visitor.objects.filter(
        status='IN'
    ).count()

    checked_out = Visitor.objects.filter(
        status='OUT'
    ).count()

    context = {
        'total_visitors': total_visitors,
        'inside_visitors': inside_visitors,
        'checked_out': checked_out,
    }

    return render(
        request,
        'gateapp/dashboard.html',
        context
    )


def visitor_list(request):

    visitors = Visitor.objects.all().order_by('-check_in')

    return render(
        request,
        'gateapp/visitor_list.html',
        {'visitors': visitors}
    )


def register_visitor(request):

    if request.method == 'POST':

        form = VisitorForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('visitor_list')

    else:

        form = VisitorForm()

    return render(
        request,
        'gateapp/visitor_form.html',
        {'form': form}
    )


def check_out(request, visitor_id):

    visitor = get_object_or_404(
        Visitor,
        id=visitor_id
    )

    visitor.check_out = timezone.now()
    visitor.status = 'OUT'

    visitor.save()

    return redirect('visitor_list')