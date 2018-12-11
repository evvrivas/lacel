def plotResults(request,poll_id):
	import matplotlib
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter
	fig = Figure()

	ax=fig.add_subplot(1,1,1)
	p = get_object_or_404(Poll, pk=poll_id) # Get the poll object from django

	x = matplotlib.numpy.arange(1,p.choice_set.count())
	choices = p.choice_set.all()

	votes = [choice.votes for choice in choices]
	names = [choice.choice for choice in choices]


	numTests = p.choice_set.count()
	ind = matplotlib.numpy.arange(numTests) # the x locations for the groups

	cols = ['red','orange','yellow','green','blue','purple','indigo']*10

	cols = cols[0:len(ind)]
	ax.bar(ind, votes,color=cols)


	ax.set_xticks(ind + 0.5)
	ax.set_xticklabels(names)


	ax.set_xlabel("Choices")
	ax.set_ylabel("Votes")

	#ax.set_xticklabels(names)

	title = u"Dynamically Generated Results Plot for poll: %s" % p.question
	ax.set_title(title)


	#ax.grid(True)
	canvas = FigureCanvas(fig)
	response = HttpResponse(content_type='image/png')

	canvas.print_png(response)
	return response