$(document).ready(function() {
    // =============================GET REQUEST=============================   
    // Settings
    var url = "/get_system_info";
    setInterval(function() {
        $.getJSON(url, function(jsondata) {
            var data = jsondata.result;
            $.each(data, function(key, val) {
                if (key === "timestamp") {
                    $("#cpu_usage").html(val);
                } else if (key === "disk_usage") {
                    $("#disk_usage").html(val);
                } else {}
            });
        });
    }, 1000);
});