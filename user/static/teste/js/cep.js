    $("input[name=cep]").blur(function() {
        var cep = $(this).val().replace(/[^0-9]/, '');
        var url = 'https://correiosapi.apphb.com/cep/'+cep;
        $.ajax({
            url: url,
            type: "GET",
            dataType: "jsonp",
            success: function (data) {
            $("input[name=pais]").val("Brasil");
            $("input[name=estado]").val(data.estado);
            $("input[name=cidade]").val(data.cidade);
            $("input[name=logradouro]").val(data.tipoDeLogradouro + " " + data.logradouro);


        }
        });

    });