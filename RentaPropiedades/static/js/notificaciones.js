
type = ['primary', 'info', 'success', 'warning', 'danger'];

notificaciones = {
    showNotificationSuccess: function(message) {

        $.notify({
            icon: "nc-icon nc-app",
            message: message

        }, {
            type: 'success',
            timer: 8000,
            placement: {
                from: 'top',
                align: 'center'
            }
        });
    },

    showNotificationDanger: function(message) {
        color = rgb(224, 92, 35);

        $.notify({
            icon: "nc-icon nc-app",
            message: message

        }, {
            type: 'warning',
            timer: 8000,
            placement: {
                from: 'top',
                align: 'center'
            }
        });
    }
}