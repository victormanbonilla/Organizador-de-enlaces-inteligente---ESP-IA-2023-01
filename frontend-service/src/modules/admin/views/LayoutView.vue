<script setup lang="ts">
import SidebarComponent from '../components/SidebarComponent.vue';
import NavBarComponent from '../components/NavBarComponent.vue';
// import SettingsIcon from '../components/SettingsIcon.vue';
// import ChartIcon from '../components/ChartIcon.vue';
import HomeIcon from '../components/HomeIcon.vue';
// import FormIcon from '../components/FormIcon.vue';
import { keyFormState } from '../utils/formKey';
import { provide, ref } from 'vue';

const icons = [
  { name: 'Home', component: HomeIcon, path: '/admin/home' },
  // { name: 'Tables', component: FormIcon, path: '/admin/form' },
  // { name: 'Analytics', component: ChartIcon, path: '/admin/analytics' },
  // { name: 'Settings', component: SettingsIcon, path: '/admin/settings' },
];

const modalState = ref(false);
const setModalState = () => (modalState.value = !modalState.value);

provide(keyFormState, [modalState, setModalState]);
</script>

<template>
  <div class="layout-container">
    <!-- Sidebar -->
    <div class="sidebar-container">
      <SidebarComponent :icons="icons" />
    </div>

    <div class="router-container">
      <div class="navbar-container">
        <NavBarComponent
          :modal-state="modalState"
          @update="($event) => (modalState = $event)"
        />
      </div>

      <RouterView />
    </div>
  </div>
</template>

<style scoped>
.layout-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  height: 100%;
  width: 100%;
  background-color: #e6e8ea;
}

.sidebar-container {
  width: 4.5%;
  height: 95%;
  position: relative;
}

.router-container {
  width: 92%;
  height: 95%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}

.navbar-container {
  width: 98%;
  height: 10%;
}
</style>
