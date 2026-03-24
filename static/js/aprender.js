// 1. BUSCADOR EN TIEMPO REAL
document.addEventListener('DOMContentLoaded', function() {
    const buscador = document.getElementById('buscador');
    const btnBuscar = document.getElementById('btn-buscar');
    const recursos = document.querySelectorAll('.recurso-card');
    
    if (buscador) {
        // Búsqueda mientras escribes
        buscador.addEventListener('keyup', function(e) {
            filtrarRecursos(this.value);
        });
        
        // Búsqueda al hacer clic en el botón
        btnBuscar.addEventListener('click', function() {
            filtrarRecursos(buscador.value);
        });
    }
    
    function filtrarRecursos(texto) {
        texto = texto.toLowerCase().trim();
        
        recursos.forEach(recurso => {
            const titulo = recurso.querySelector('h3').textContent.toLowerCase();
            const descripcion = recurso.querySelector('p').textContent.toLowerCase();
            const categoria = recurso.querySelector('.recurso-categoria').textContent.toLowerCase();
            
            if (titulo.includes(texto) || descripcion.includes(texto) || categoria.includes(texto)) {
                recurso.style.display = 'flex';
                // Animación de aparición
                recurso.style.animation = 'fadeIn 0.5s ease';
            } else {
                recurso.style.display = 'none';
            }
        });
        
        // Mostrar mensaje si no hay resultados
        const grid = document.getElementById('recursos-grid');
        const visibles = document.querySelectorAll('.recurso-card[style="display: flex;"]');
        
        let mensaje = document.getElementById('sin-resultados');
        if (visibles.length === 0) {
            if (!mensaje) {
                mensaje = document.createElement('p');
                mensaje.id = 'sin-resultados';
                mensaje.textContent = 'No encontramos recursos con esa búsqueda. ¡Prueba con otras palabras!';
                mensaje.style.textAlign = 'center';
                mensaje.style.padding = '2rem';
                grid.appendChild(mensaje);
            }
        } else if (mensaje) {
            mensaje.remove();
        }
    }
    
    // 2. NEWSLETTER CON VALIDACIÓN Y MENSAJE
    const newsletterForm = document.getElementById('newsletter-form');
    
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const email = document.getElementById('email').value;
            const mensaje = document.getElementById('newsletter-mensaje');
            
            // Validación simple de email
            if (!isValidEmail(email)) {
                mostrarMensaje('Por favor, ingresa un correo válido', 'error');
                return;
            }
            
            // Simular envío (aquí conectarías con tu backend)
            mostrarMensaje('¡Gracias por suscribirte! Revisa tu correo', 'exito');
            newsletterForm.reset();
            
            // Aquí podrías hacer un fetch a tu backend
            /*
            fetch('/api/suscribir/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({email: email})
            })
            .then(response => response.json())
            .then(data => {
                mostrarMensaje(data.mensaje, 'exito');
            })
            .catch(error => {
                mostrarMensaje('Hubo un error, intenta más tarde', 'error');
            });
            */
        });
    }
    
    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    function mostrarMensaje(texto, tipo) {
        const mensaje = document.getElementById('newsletter-mensaje');
        mensaje.textContent = texto;
        mensaje.className = 'newsletter-mensaje ' + tipo;
        mensaje.style.display = 'block';
        
        setTimeout(() => {
            mensaje.style.display = 'none';
        }, 5000);
    }
    
    // 3. FILTRO POR CATEGORÍA (para la página de categoría)
    const filtroBtns = document.querySelectorAll('.filtro-btn');
    
    filtroBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const categoria = this.dataset.categoria;
            
            // Activar/desactivar botones
            filtroBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            
            // Filtrar recursos
            recursos.forEach(recurso => {
                if (categoria === 'todos' || recurso.dataset.categoria === categoria) {
                    recurso.style.display = 'flex';
                } else {
                    recurso.style.display = 'none';
                }
            });
        });
    });
    
    // 4. ANIMACIONES AL HACER SCROLL
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.recurso-card, .categoria-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'all 0.6s ease';
        observer.observe(el);
    });
});