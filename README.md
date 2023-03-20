# H23-GR1-E2-BdeBCentreAide
<!DOCTYPE hmtl>
<html lang="en">
    <head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Display Web Cam Stream</title>

			<style>
				h1{
					font-family: sans-serif;
					text-align: center;
				}

				#videoElement{
					width: 500px;
					height: 375px;
					background-color: grey;
				}

				#container{
					margin: 0px auto;
					width: 500px;
					height: 375px;
					border: 10px black solid;
				}
			</style>
    </head>
    <body>
			<h1>WebCam test</h1>
			<div id="container">
				<video autoplay="true" id="videoElement">

				</video>
			</div>

			<script>
				let video = document.querySelector("#videoElement")

				if(navigator.mediaDevices.getUserMedia){
					navigator.mediaDevices.getUserMedia({video: true})
					.then(function (stream){
						video.srcObject = stream;

					})
					.catch(function(error){
						console.log("ERROR!")
					})
				} else {
					con.console.log("getUserMedia not supported!");
				}

			</script>

    </body>
</html>
