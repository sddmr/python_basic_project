from plyer import notification

notification.notify(
    title = 'Hatirlatma!',
    message = 'Bu bir bildirim ornegidir!',
    app_name = 'Notification',
    timeout = 10, # Bildirimin görünme süresi (saniye)
)