const getTitleMessageFromCategory = category => {
    const titles = {
        'success' : 'Bien Hecho',
        'warning' : 'Atencion',
        'info' : 'Atencion',
        'error' : 'Oops...!',

    }
    return titles[category]
}

function showMessageAlert(category, message) {
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer)
          toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
      })
      
      Toast.fire({
        icon: category,
        title: getTitleMessageFromCategory(category),
        text: message
      })
}
