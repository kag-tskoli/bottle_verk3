<!DOCTYPE html>
<html>
<head>
	<title>{{frettir[int(n)]['heading']}}</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="/static/css/styles.css">
</head>
<body>
	% include("tpl/header.tpl")
		
	<section>
		<div class="col1">
			<h2>{{frettir[int(n)]['heading']}}</h2>
			<img src="/static/img/{{frettir[int(n)]['image']}}">
		</div>
		<div class="col2">
			<p>{{frettir[int(n)]['content']}}</p>
			<p>{{frettir[int(n)]['reporter']}}</p>
			<br>
			<a href="/b">Til baka</a>
		</div>
	</section>

	% include("tpl/footer.tpl")
</body>
</html>