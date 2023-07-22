$(document).ready(function() {
    $("#tags").change(function() {
        var selectedTag = $(this).val();
        $.ajax({
            type: "POST",
            contentType: "application/json",
            url: "/get_images",
            data: JSON.stringify({ tag: selectedTag }),
            dataType: "json",
            success: function(data) {
                displayImages(data);
            },
            error: function(error) {
                console.log("Error fetching images: ", error);
            }
        });
    });
});

function displayImages(images) {
    var imageContainer = $("#image-container");
    imageContainer.empty();
    images.forEach(function(image) {
        var imgTag = $("<img>").attr("src", "static/images/" + image[0]);
        imgTag.attr("alt", "Image");
        imageContainer.append(imgTag);
    });
}
