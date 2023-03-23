<script setup lang="ts">
import { useAuthStore } from '../composables/useAuthStore';
import { computed, markRaw } from 'vue';
import { useForm } from 'vee-validate';
import { object, string } from 'yup';

import GoogleButtonComponent from '../components/GoogleButtonComponent.vue';
import ModalComponent from '../components/ModalComponent.vue';
import InputLogin from '../components/InputLogin.vue';

const { startLogin } = useAuthStore();
const schema = markRaw(object({
	user: 
    string()
    .required('Please enter your user'),
	password: 
    string()
		.required('Please enter your password')
		.min(3, 'Please enter a minimun value of 3 characters'),
}));

const { handleSubmit, errors } = useForm({
	initialValues: {
		user: '',
		password: ''
	},
	validationSchema: schema
});

const onSubmit = handleSubmit(({ user, password }) => {
	startLogin(user, password)
});

const invalid = computed(() => !!Object.keys(errors.value).length);
</script>
<template>
  <div class="login-container">
    <ModalComponent>
      <h1 class="login-title">
        Login
      </h1>

      <form
        class="login-form"
        autocomplete="off"
        @submit.prevent="onSubmit"
      >
        <!-- Input Email -->
        <InputLogin
          id="custom-user"
          name="user"
          type="text"
          label="User"
          placeholder="admin123456"
        />
        <!-- Input Password -->
        <InputLogin
          id="custom-password"
          label="Password"
          name="password"
          type="password"
          placeholder="●●●●●●●●"
        />
        <!-- Submit Button -->
        <button
          class="submit-button"
          type="submit"
          :disabled="invalid"
        >
          Sign in
        </button>

        <!-- Divider -->
        <span class="divider-text">OR</span>

        <!-- Google Button -->
        <GoogleButtonComponent />

        <RouterLink
          to="/auth/register"
          class="register-hyperlink"
        >
          Are you registered?
        </RouterLink>
      </form>
    </ModalComponent>
  </div>
</template>

<style scoped>
.login-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}
.login-form {
	display: flex;
	flex-direction: column;
	align-items: center;
	height: 80%;
	width: 88%;
}
.submit-button {
	width: 94%;
	height: 12%;
	background-color: #598bff;
	border-color: transparent;
	color: #ffffff;
	font-size: 12px;
	border-radius: 10px;
	margin-top: 10px;
	cursor: pointer;
	transition: background 0.1s;
}
.submit-button:enabled:active {
	background-color: #507de6;
}

.submit-button:disabled {
  background-color: #4871cf;
  cursor: default;
}
.divider-text {
	color: #92929d;
	font-size: 12px;
	margin: 10px 0;
}
.login-title {
	font-size: 18px;
}
.register-hyperlink {
  text-decoration: none;
  padding-top: 3px;
  font-size: 13px;
  color: #7d79e6;
  font-weight: 500;
}
</style>