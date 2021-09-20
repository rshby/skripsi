<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <!-- Bootstrap CSS -->
    <link href="css/bootstrap.css" rel="stylesheet" />

    <!-- My Css -->
    <link rel="stylesheet" href="style.css" />

    <title>Sistem Prediksi Penyakit Jantung</title>
</head>

<body>
    <!-- navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark shadow">
        <div class="container">
            <a class="navbar-brand" href="index.php">Sistem Prediksi Penyakit Jantung</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav margin ms-auto">
                    <a class="nav-link" aria-current="page" href="/">Home</a>
                    <a class="nav-link" href="information">Information</a>
                    <a class="nav-link active" href="data">Data</a>
                </div>
            </div>
        </div>
    </nav>
    <!-- akhir navbar -->

    <!-- Jumbotron -->
    <section class="jumbotron jumbotron-fluid text-center">
        <div class="container">
            <img src="images/gambar_data.png" alt="gambar jantung" width="250">
            <h1 class="display-4">Data Yang Digunakan</h1>
        </div>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
            <path fill="#fff" fill-opacity="1" d="M0,32L21.8,48C43.6,64,87,96,131,128C174.5,160,218,192,262,192C305.5,192,349,160,393,144C436.4,128,480,128,524,138.7C567.3,149,611,171,655,165.3C698.2,160,742,128,785,138.7C829.1,149,873,203,916,213.3C960,224,1004,192,1047,154.7C1090.9,117,1135,75,1178,64C1221.8,53,1265,75,1309,112C1352.7,149,1396,203,1418,229.3L1440,256L1440,320L1418.2,320C1396.4,320,1353,320,1309,320C1265.5,320,1222,320,1178,320C1134.5,320,1091,320,1047,320C1003.6,320,960,320,916,320C872.7,320,829,320,785,320C741.8,320,698,320,655,320C610.9,320,567,320,524,320C480,320,436,320,393,320C349.1,320,305,320,262,320C218.2,320,175,320,131,320C87.3,320,44,320,22,320L0,320Z"></path>
        </svg>
    </section>
    <!-- Akhir Jumbotron -->

    <section id="isi_informasi" class="container">
        <div class="row justify-content-center mb-2">
            <div class="col-4 text-center">
                <h3>Dataset yang digunakan</h3>
            </div>
        </div>
        <div class="row justify-content-center tabel_data">
            <div class="col-12">
                <table class="table table-striped">
                    <thead class="table-dark">
                        <tr>
                            <th scope="col">Umur</th>
                            <th scope="col">Jenis Kelamin</th>
                            <th scope="col">CP</th>
                            <th scope="col">Trestbps</th>
                            <th scope="col">Chol</th>
                            <th scope="col">Fbs</th>
                            <th scope="col">Restecg</th>
                            <th scope="col">Thalach</th>
                            <th scope="col">Exang</th>
                            <th scope="col">Oldpeak</th>
                            <th scope="col">Slope</th>
                            <th scope="col">Ca</th>
                            <th scope="col">Thal</th>
                            <th scope="col">Target</th>
                        </tr>
                    </thead>
                    <tbody id="isi_data">
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <!-- Hasil Prediksi -->
    <section id="hasil_prediksi">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
            <path fill="#9fc55a" fill-opacity="1" d="M0,64L26.7,74.7C53.3,85,107,107,160,101.3C213.3,96,267,64,320,48C373.3,32,427,32,480,42.7C533.3,53,587,75,640,117.3C693.3,160,747,224,800,229.3C853.3,235,907,181,960,181.3C1013.3,181,1067,235,1120,224C1173.3,213,1227,139,1280,101.3C1333.3,64,1387,64,1413,64L1440,64L1440,320L1413.3,320C1386.7,320,1333,320,1280,320C1226.7,320,1173,320,1120,320C1066.7,320,1013,320,960,320C906.7,320,853,320,800,320C746.7,320,693,320,640,320C586.7,320,533,320,480,320C426.7,320,373,320,320,320C266.7,320,213,320,160,320C106.7,320,53,320,27,320L0,320Z"></path>
        </svg>
    </section>
    <!-- Akhir Hasil Prediksi -->

    <!-- Footer -->
    <footer>

        <h5 class="text-center">Reo Sahobby</h5>
    </footer>
    <!-- Akhir Footer -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="js/bootstrap.bundle.js"></script>

    <!-- JavaScript unutk Ajax -->
    <script src="jquery-3.6.0.js"></script>
    <script>
        $(document).ready(function() {
            var settings = {
                "url": "http://localhost:8005/heart/all",
                "method": "GET",
                "timeout": 0,
            };

            $.ajax(settings).done(function(response) {
                console.log(response);
                $.each(response, function(key, value) {
                    $('#isi_data').append(
                        "<tr class='text-center'>" +
                        '<td>' + value.age + '</td>' +
                        '<td>' + value.sex + '</td>' +
                        '<td>' + value.cp + '</td>' +
                        '<td>' + value.trestbps + '</td>' +
                        '<td>' + value.chol + '</td>' +
                        '<td>' + value.fbs + '</td>' +
                        '<td>' + value.restecg + '</td>' +
                        '<td>' + value.thalach + '</td>' +
                        '<td>' + value.exang + '</td>' +
                        '<td>' + value.oldpeak + '</td>' +
                        '<td>' + value.slope + '</td>' +
                        '<td>' + value.ca + '</td>' +
                        '<td>' + value.thal + '</td>' +
                        '<td>' + value.target + '</td>' +
                        '</tr>'
                    );


                });
            });
        });
    </script>
</body>

</html>