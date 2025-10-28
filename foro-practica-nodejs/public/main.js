// Funciones utilitarias
function randChoice(arr){return arr[Math.floor(Math.random()*arr.length)]}
function randomNametag(){
  // Genera un nombre aleatorio combinando adjetivo + animal + número
  const adjectives = ['Luz','Viajero','Menta','Sol','Nube','Eco','Brisa','Rayo','Clave','Pixel','Lobo','Gato','Rosa','Zumo'];
  const animals = ['Zorro','Gaviota','Toro','Tigre','Colibri','Iguana','Búho','Perro','Lince','Orca'];
  return `${randChoice(adjectives)}${randChoice(animals)}${Math.floor(Math.random()*90+10)}`;
}
function randomColor(){
  // Elije un color aleatorio de la lista
  const colors = ['#6f42c1','#0d6efd','#198754','#fd7e14','#dc3545','#20c997','#6610f2','#e83e8c'];
  return randChoice(colors);
}

// Persistencia: guardar el nametag en localStorage
const STORAGE_KEY = 'foro_nametag_v1';
function ensureNametag(){
  // Devuelve el nametag guardado, o genera y guarda uno nuevo si no existe
  const raw = localStorage.getItem(STORAGE_KEY);
  if(raw) return JSON.parse(raw);
  const nt = { nametag: randomNametag(), color: randomColor() };
  localStorage.setItem(STORAGE_KEY, JSON.stringify(nt));
  return nt;
}

// Renderizado de un solo post
function renderPost(post){
  // Crea el contenedor del post
  const div = document.createElement('div');
  div.className = 'card mb-3 post-card shadow-sm';

  // Normaliza la review (0..10) y construye el HTML de estrellas poniendo data-value en cada estrella
  const raw = Number(post.review) || 0;
  const review = Math.max(0, Math.min(10, Math.round(raw)));
  // Cada estrella puede seleccionarse hasta 5 (media en media para 0~10)
  let starsHtml = '';
  for(let i=1; i<=10; i+=2){
    const active = i <= review ? 'text-warning' : 'text-muted';
    const full = i+1 <= review;
    // Si no logueado, las estrellas no son clickable
    const starClass = isLoggedIn() ? 'clickable-star' : '';
    const disableAttr = isLoggedIn() ? '' : ' style="opacity:0.4;pointer-events:none;"';
    starsHtml += `<i class="bi ${full?"bi-star-fill":"bi-star-half"} ${active} ${starClass}" aria-hidden="true" data-value="${i}"${disableAttr}></i>`;
  }

  // Construye el HTML de la tarjeta del post
  div.innerHTML = `
    <div class="card-body d-flex gap-3 align-items-start">
      <div class="flex-shrink-0">
        <div class="avatar rounded-circle" style="background:${post.avatarColor}"></div>
      </div>
      <div class="flex-grow-1">
        <div class="d-flex align-items-center gap-2 mb-1">
          <div class="nametag text-dark">${escapeHtml(post.nametag)}</div>
          <small class="text-muted">• ${new Date(post.createdAt).toLocaleString()}</small>
        </div>
        <div class="mb-1">
          <span class="stars clickable-stars" aria-hidden="true" data-id="${post.id}">${starsHtml}</span>
          <small class="text-muted ms-2">(${review}/10)</small>
        </div>
        <div class="text-break">${escapeHtml(post.text)}</div>
      </div>
      <div class="post-actions d-flex flex-column align-items-center">
        <button title="Editar" data-action="edit" data-id="${post.id}" class="btn btn-sm btn-outline-primary icon-btn" ${isLoggedIn()?'':'disabled style="pointer-events:none;opacity:0.4;"'}>
          <i class="bi bi-pencil" aria-hidden="true"></i>
        </button>
        <button title="Eliminar" data-action="delete" data-id="${post.id}" class="btn btn-sm btn-outline-danger icon-btn" ${isLoggedIn()?'':'disabled style="pointer-events:none;opacity:0.4;"'}>
          <i class="bi bi-trash" aria-hidden="true"></i>
        </button>
      </div>
    </div>
  `;
  return div;
}

// Escapa caracteres peligrosos para evitar XSS
function escapeHtml(s){
  return s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
}

// --- Lógica principal de la aplicación frontend ---
const tag = ensureNametag(); // Nombre y color actuales
// Renderizamos el badge de usuario
// Mostramos el color y nombre en la interfaz

// Asignamos los datos al badge del usuario actual
// y al avatar principal del formulario
// (crear post y editar post)
document.getElementById('nametag-badge').textContent = tag.nametag;
document.getElementById('nametag-badge').style.background = tag.color;
document.getElementById('avatar').style.background = tag.color;

// Carga todos los posts actuales y los muestra en pantalla
async function loadPosts(){
  const res = await fetch('/api/posts');
  const data = await res.json();
  const container = document.getElementById('posts');
  container.innerHTML = '';
  if(data.length === 0){
    container.innerHTML = '<div class="text-muted">No hay posts todavía. Sé el primero.</div>';
    return;
  }
  data.forEach(p => container.appendChild(renderPost(p)));
}

document.getElementById('post-form').addEventListener('submit', async (e) =>{
  e.preventDefault();
  const textEl = document.getElementById('post-text');
  const text = textEl.value.trim();
  if(!text) return;
  // Si se está en modo edición, hace PATCH al post existente
  if(window.__editingId){
    const id = window.__editingId;
    const res = await fetch(`/api/posts/${id}`, { method: 'PATCH', headers: {'content-type':'application/json'}, body: JSON.stringify({ text, nametag: tag.nametag, avatarColor: tag.color })});
    if(res.ok){
      window.__editingId = null;
      document.querySelector('#post-form button[type="submit"]').textContent = 'Publicar';
      textEl.value = '';
      await loadPosts();
      return;
    } else {
      const err = await res.json().catch(()=>({error:'error'}));
      alert(err.error || 'Error al editar');
      return;
    }
  }

  // Si no es edición, es un post nuevo
  const body = { text, nametag: tag.nametag, avatarColor: tag.color };
  const res = await fetch('/api/posts', { method: 'POST', headers: {'content-type':'application/json'}, body: JSON.stringify(body)});
  if(res.ok){
    textEl.value = '';
    await loadPosts();
  } else {
    const err = await res.json().catch(()=>({error:'error'}));
    alert(err.error || 'Error al publicar');
  }
});

// Maneja clicks en botones de editar y eliminar de los posts
// Delegation para que funcione con posts creados dinámicamente
document.getElementById('posts').addEventListener('click', (e) =>{
  const btn = e.target.closest('button[data-action]');
  if(!btn) return;
  const action = btn.getAttribute('data-action');
  const id = btn.getAttribute('data-id');
  if(action === 'delete'){
    // Confirma antes de eliminar
    openConfirm('Eliminar post', '¿Deseas eliminar este post? Esta acción no se puede deshacer.', async () => {
      const res = await fetch(`/api/posts/${id}`, { method: 'DELETE' });
      if(res.status === 204){
        await loadPosts();
      } else {
        const err = await res.json().catch(()=>({error:'error'}));
        alert(err.error || 'Error al eliminar');
      }
    });
  } else if(action === 'edit'){
    // Confirma antes de editar y carga contenido al formulario
    openConfirm('Editar post', '¿Deseas editar este post? Al confirmar se cargará el contenido en el formulario.', async () => {
  // Busca el post actual en el servidor
  const res = await fetch(`/api/posts`);
  const data = await res.json();
  const post = data.find(p => String(p.id) === String(id));
  if(!post){ alert('Post no encontrado'); return; }
  document.getElementById('post-text').value = post.text;
  window.__editingId = post.id; // Usar el id numérico real
  document.querySelector('#post-form button[type="submit"]').textContent = 'Guardar cambios';
  document.getElementById('post-text').scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }
});

// Delegación para clicks en estrellas
// (esto va después del addEventListener para editar/eliminar en posts)
document.getElementById('posts').addEventListener('click', async function(e){
  if(!isLoggedIn()) return;
  // Si clickea una estrella
  if(e.target.classList && e.target.classList.contains('clickable-star')){
    const star = e.target;
    const value = Number(star.getAttribute('data-value'));
    const span = star.closest('.stars');
    const postId = span.getAttribute('data-id');
    // PATCH al backend solo review
    await fetch(`/api/posts/${postId}`,{
      method:'PATCH',
      headers:{'content-type':'application/json'},
      body: JSON.stringify({ review: value })
    });
    await loadPosts();
  }
});

// Función para mostrar un modal de confirmación antes de eliminar o editar
function openConfirm(title, body, onConfirm){
  const modalEl = document.getElementById('confirmModal');
  const modal = new bootstrap.Modal(modalEl);
  document.getElementById('confirmModalLabel').textContent = title;
  document.getElementById('confirmModalBody').textContent = body;
  const confirmBtn = document.getElementById('confirmModalConfirm');

  const handler = async () =>{ modal.hide(); confirmBtn.removeEventListener('click', handler); await onConfirm(); };
  confirmBtn.addEventListener('click', handler);
  modal.show();
}

// --- Gestión de login visual y control de sesión ---
function isLoggedIn() {
  return localStorage.getItem('foro_logged_in') === '1';
}
function setLoggedIn(logged) {
  if (logged) localStorage.setItem('foro_logged_in', '1'); else localStorage.removeItem('foro_logged_in');
}
function renderAuthUI() {
  const badge = document.getElementById('nametag-badge');
  const postForm = document.getElementById('new-post');
  const loginBtn = document.getElementById('login-modal-btn');
  if (isLoggedIn()) {
    if (badge) {
      badge.textContent = tag.nametag;
      badge.style.background = tag.color;
      badge.style.display = '';
    }
    if (postForm) postForm.style.display = '';
    if (loginBtn) loginBtn.textContent = 'Cerrar sesión';
  } else {
    if (badge) badge.style.display = 'none';
    if (postForm) postForm.style.display = 'none';
    if (loginBtn) loginBtn.textContent = 'Iniciar sesión';
  }
  loadPosts(); // Al cerrar/abrir sesión, recarga/posts refrescan interacciones
}
document.addEventListener('DOMContentLoaded', function() {
  renderAuthUI();
  // Modifica acción botón login/cerrar sesión
  const loginBtn = document.getElementById('login-modal-btn');
  if (loginBtn) {
    loginBtn.addEventListener('click', function(ev) {
      if (isLoggedIn()) {
        setLoggedIn(false);
        renderAuthUI();
        ev.preventDefault();
      }
    });
  }
});
// Al hacer login exitoso, guardar flag y refrescar UI
// Dentro del submit de login:
// if(resp.ok) {
//   setLoggedIn(true);
//   renderAuthUI();
//   bootstrap.Modal.getOrCreateInstance(document.getElementById('loginModal')).hide();
//   alert('¡Sesión iniciada para ' + nombre + '!');
// } else {
//   const err = await resp.json().catch(()=>({error:'Error'}));
//   alert(err.error || 'Error al iniciar sesión');
// }

// --- Lógica para el modal de inicio de sesión ---
document.addEventListener('DOMContentLoaded', function() {
  const loginUsername = document.getElementById('login-username');
  const loginModalBtn = document.getElementById('login-modal-btn');
  const loginForm = document.getElementById('login-form');
  if (loginUsername && tag && tag.nametag) {
    loginUsername.value = tag.nametag;
  }
  if (loginModalBtn) {
    loginModalBtn.addEventListener('click', function() {
      if (loginUsername && tag) loginUsername.value = tag.nametag;
      if(document.getElementById('login-password')) {
        document.getElementById('login-password').value = '';
      }
    });
  }
  if (loginForm) {
    loginForm.addEventListener('submit', function(e) {
      e.preventDefault();
      // Aquí puedes capturar los valores y hacer futuras validaciones
      const nombre = loginUsername.value;
      const password = document.getElementById('login-password').value;
      if (!password) {
        alert('Ingresa una contraseña.');
        return;
      }
      // Llamar al backend para autenticar usuario
      fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: nombre, password })
      })
      .then(async resp => {
        if(resp.ok) {
          setLoggedIn(true);
          renderAuthUI();
          bootstrap.Modal.getOrCreateInstance(document.getElementById('loginModal')).hide();
          alert('¡Sesión iniciada para ' + nombre + '!');
        } else {
          const err = await resp.json().catch(()=>({error:'Error'}));
          alert(err.error || 'Error al iniciar sesión');
        }
      });
    });
  }
});

// Carga los posts al inicio
document.addEventListener('DOMContentLoaded', loadPosts);
// O si se asegura que el DOM ya está cargado:
loadPosts();
