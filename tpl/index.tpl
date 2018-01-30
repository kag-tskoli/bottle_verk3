<!DOCTYPE html>
<html>
<head>
	<title>Fréttasíðan mín</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="/static/css/styles.css">
</head>
<body>
	% include("tpl/header.tpl")
		
	<section>
		<div class="col1">
			<h2>{{frettir[0]['heading']}}</h2>
			<img src="/static/img/{{frettir[0]['image']}}">
		</div>
		<div class="col2">
			<ul>
				<li><a href="/frett/0">Frétt 1</a></li>
				<li><a href="/frett/1">Frétt 2</a></li>
				<li><a href="/frett/2">Frétt 3</a></li>
				<li><a href="/frett/3">Frétt 4</a></li>
			</ul>
		</div>
	</section>

	% include("tpl/footer.tpl")
</body>
</html>