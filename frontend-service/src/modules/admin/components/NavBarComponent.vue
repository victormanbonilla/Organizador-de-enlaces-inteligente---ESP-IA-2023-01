<script setup lang="ts">
import { inject } from 'vue';
import { useAuthStore } from '../../auth/composables/useAuthStore';
import { keyFormState } from '../utils/formKey';
import UserIcon from './UserIcon.vue';

const { user, startLogout } = useAuthStore();
const rawUser = { ...user.value };

const [, setFormState] = inject(keyFormState)!;

</script>

<template>
  <div class="navbar-sub-container">
    <button
      class="btn-add-table"
      type="button"
      @click="setFormState"
    >
      Add Table
    </button>
    <div class="user-utils">
      <div class="user-container">
        <UserIcon />
      </div>
      <p style="padding-left: 5px; font-weight: 500; color: #5c5b5b">
        {{ rawUser.name }}
      </p>
      <button
        class="btn-singout"
        @click="startLogout()"
      >
        Sign Out
      </button>
    </div>
  </div>
</template>

<style scoped>
.navbar-sub-container {
  width: 100%;
  height: 80%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  background-color: #ffffff;
  border-radius: 20px;
  box-shadow: 0px 10px 15px -3px rgba(0, 0, 0, 0.1);
  padding-right: 15px;
}
.user-container {
  background-color: green;
  height: 45px;
  width: 45px;
  border-radius: 100%;
  background-color: white;
  color: #598bff;
  border: 3px solid #598bff;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.btn-singout {
  margin-left: 15px;
  background-color: #598bff;
  color: white;
  border-color: transparent;
  padding: 3px 10px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
  transition: all 0.1s;
}
.btn-singout:hover {
  background-color: #7ca1f7;
}
.btn-singout:active {
  background-color: #607cbf;
}
.user-utils {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.btn-add-table {
  margin-left: 15px;
  background-color: #9167cc;
  color: white;
  border-color: transparent;
  padding: 3px 10px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
  transition: all 0.1s;
}
.btn-add-table:hover {
  background-color: #a474e8;
}
.btn-add-table:active {
  background-color: #7553a6;
}
</style>
