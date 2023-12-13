function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');
  
    if (taskInput.value !== '') {
      const li = document.createElement('li');
      li.innerHTML = `${taskInput.value} <span class="delete" onclick="removeTask(this)">❌</span>`;
      taskList.appendChild(li);
      taskInput.value = '';
    }
  }
  
  function removeTask(element) {
    element.parentElement.remove();
  }
  