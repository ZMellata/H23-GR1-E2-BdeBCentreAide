# H23-GR1-E2-BdeBCentreAide

/* HTML */
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Centre d'aide</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css" integrity="sha512-SzlrxWUlpfuzQ+pcUCosxcglQRNAq/DZjVsC0lE40xsADsfeQoEypE+enwcOiGjk/bSuGGKHEyjSoQ1zVisanQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="style.css">
</head>

<body>

    <header>
        <div class="navbar">
            <nav class="navigation hide">
                <ul class="nav-list">
                    <span class="close-icon"><i class="fa-solid fa-rectangle-xmark"></i></span>
                    <li class="nav-item">
                        <a href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a href="#">Forum</a>
                    </li>
                    <li class="nav-item">
                        <a href="#">Detail</a>
                    </li>
                </ul>
            </nav>
            <a href="" class="bar-icon"><i class="fa-solid fa-bars"></i></a>
            <div class="brand">My Forum</div>
        </div>
    </header>

    <div class="container">
        <div class="subforum">
            <div class="subforum-title">
                <h1>General Information</h1>
            </div>
            <div class="subforum-row">
                <div class="subforum-icon subforum-column center">
                    <i class="fa-solid fa-school"></i>
                </div>
                <div class="subforum-description subforum-column">
                    <h1><a href="">Description Title : </a></h1>
                    <p>Description Content : bla vlawnf ejiwnfijewnfi jinefwinf hefbwbfkwkfkwjef wkjefjkwenfjwnjfnwjkef jwefnjwenfjewnfjkwnfnw </p>

                </div>
                <div class="subforum-stats subforum-column center">
                    <span>24 Posts | 15 Topics</span>
                </div>
                <div class="subforum-info subforum-column">
                    <b><a href="">Last Post</a></b> by <a href="">JustAUser</a>
                    <br>Écrit le : 6 Mars 2023
                </div>
            </div>
        </div>
    </div>
    <script src="main.js"></script>
</body>
</html>

/* CSS */
/* global */

*{
    box-sizing: border-box;
}

html{
    font-size: 16px;
    font-family: Arial, Helvetica, sans-serif;
    background-color: darkgrey;
    color: black;
}

a{
    color: brown;
    font-weight: bolder;
    text-decoration: none;
    
}

h1{
    font-size: 22px;
    font-weight: bolder;
}

p{
    font-size: 16px;
}

span{
    font-weight: bolder;
}

/* home.html */

.container{
    margin: 10px;
    padding: 10px;
    
}

.subforum{
    margin-top: 10px;
}

.subforum-title{
    background-color: white;
    padding: 5px;
    border-radius: 5px;
    margin: 4px;

}

.subforum-row{
    display: grid;
    grid-template-columns: 7% 60% 13% 20%;
}

.subforum-column{
    padding: 5px;
    margin: 4px;
    border-radius: 5px;
    background-color: grey;
}

.subforum-description *{
    margin-block: 0px;
}

.center{
    display: flex;
    justify-content: center;
    align-items: center;
}

.subforum-icon{
    font-size: 50px;
}

/* Pour cellulaires */
@media screen and (max-width: 460px){
    .container{
        margin: 10px;
        padding: 10px;
    }

    .subforum-row{
        display: grid;
        grid-template-columns: 25% 75%;
        grid-template-rows: 65% 35%;
    }

    .subforum-description *{
        font-size: 14px;
    }

    .subforum-stats{
        font-size: 14px;
    }

    .subforum-info{
        font-size: 14px;
    }

   
}

/*Pour tablets */
@media screen and (min-width: 461px) and (max-width: 1024px){
    .container{
        margin: 15px;
        padding: 15px;
    }

    .subforum-row{
        display: grid;
        grid-template-columns: 10% 60% 10% 20%;

    }

    .subforum-icon{
        font-size: 40px;
    }

    html{
        font-size: 18px;
    }

    h1{
        font-size: 20px;
    }
}

/* navbar */

header{
    margin-inline: 10px;
}

.navbar{
    display: flex;
    align-items: center;
}

.navigation{
    background-color: wheat;
    padding: 10px;
    width: 65%;
    display: inline-block;
    border-radius: 5px;
    max-height: 80px;
    margin-right: 10px;
}

.nav-list{
    list-style-type: none;
    overflow: hidden;
}

.nav-item a{
    float: right;
    display: block;
    text-align: center;
    margin-inline: 20px;
    font-size: 20px;
    padding: 10px;
    color: black;
}

.nav-item a:hover{
    background-color: black;
}

.close-icon i{
    font-size: 40px;
    float: left;
    cursor: pointer;
}

.hide{
    display: none;
}

.bar-icon{
    font-size: 40px;
    display: inline-block;
    margin-right: 10px;
    color: black;
    cursor: pointer;
}

.brand{
    font-size: 40px;
    display: inline-block;
    font-family: Arial, Helvetica, sans-serif;
    font-weight: bolder;
}
