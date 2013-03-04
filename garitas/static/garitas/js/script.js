function shadowScreen(){
    var shadow_screen = document.getElementById("shadow_screen");
    if(shadow_screen === null) {
        var layer = document.createElement('div');
        layer.id = "shadow_screen";
        layer.style.width = '100%';
        layer.style.height ='100%';
        layer.style.position = 'fixed';
        layer.style.top = 0;
        layer.style.left = 0;
        layer.style.padding = 0;
        layer.style.margin = 0;
        layer.style.zIndex = 2;
        layer.innerHTML = "<img src='/static/garitas/img/background-alpha.png' width='100%' height='100%'>";
        document.body.appendChild(layer);
    } else {
        $("#shadow_screen").css('visibility', 'visible');
    }
}

function showFeedbackLoading(){
    $('.feedback-loading').css('visibility', 'visible');
}

function hideFeedbackLoading(){
    $('.feedback-loading').css('visibility', 'hidden');
}

function hideShadowScreen(){
    $("#shadow_screen").css('visibility', 'hidden');
}

function selectCity() {
    shadowScreen();
    $('#box_popup').show("slow");
}

function closeSelectCity(){
    hideShadowScreen();
	$('#box_popup').hide("slow");
}

function feedback(){
    shadowScreen();
    $(".feedback").show("slow");
}

function closeFeedback(){
    hideShadowScreen();
    $('.feedback').hide("slow");
}

function showResponse(response, statusText, xhr, $form)  {
    if(response['success'] === true) {
        alert("Gracias por comunicarte!");
    } else {
        alert("Error enviando el mensaje!");
    }
    $form.clearForm();
    closeFeedback();
    hideFeedbackLoading();
}

var options = {
        success: showResponse,  // post-submit callback
        dataType:  'json'
};

$(document).on('ready', function(){
  $("#contact_form").validate({
      submitHandler: function(form) {
            showFeedbackLoading();
            $(form).ajaxSubmit(options);
      },
      rules: {
          email: {
              required: true,
              email: true
          }
      }
  });
});