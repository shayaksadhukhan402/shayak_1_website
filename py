<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Brython Example</title>
    <!-- Brython library load -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.10.10/brython.min.js"></script>
</head>
<body onload="brython()">

<h2>Python in Browser with Brython</h2>

<script type="text/python">
from browser import alert
alert("হ্যালো! পাইথন এখন ব্রাউজারে চলছে।")
</script>

</body>
</html>
