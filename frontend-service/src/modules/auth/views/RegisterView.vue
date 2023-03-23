<script setup lang="ts">
import { computed, markRaw } from 'vue';
import { useForm } from 'vee-validate';
import { object, string, ref } from 'yup';

import ModalComponent from '../components/ModalComponent.vue';
import { useAuthStore } from '../composables/useAuthStore';
import InputLogin from '../components/InputLogin.vue';
import { ElMessage } from 'element-plus';

const schema = markRaw(
  object({
    user: string().required('Please enter your user'),
    password: string()
      .required('Please enter your password')
      .min(3, 'Please enter a minimun value of 3 characters'),
    passwordConfirmation: string().oneOf(
      [ref('password')],
      'Passwords must match'
    ),
  })
);

const message = (state: 'success' | 'error') => {
  ElMessage({
    showClose: true,
    message: state == 'success' ? 'Success' : 'Error, user already exists!',
    type: state,
  });
};

const { startRegister } = useAuthStore();
const { handleSubmit, errors } = useForm({
  initialValues: {
    user: '',
    password: '',
    passwordConfirm: '',
  },
  validationSchema: schema,
});

const onSubmit = handleSubmit(async ({ user, password }) => {
  const result = await startRegister(user, password);
  result ? message('success') : message('error');
});

const invalid = computed(() => !!Object.keys(errors.value).length);
</script>

<template>
  <div class="register-container">
    <ModalComponent>
      <h1 class="register-title">
        Register
      </h1>

      <form
        class="register-form"
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

        <!-- Input Repeat Password -->
        <InputLogin
          id="custom-password-confirm"
          label="Password Confirmation"
          name="passwordConfirmation"
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

        <!-- Login button -->
        <RouterLink
          to="/auth/login"
          class="login-button"
        >
          Login
        </RouterLink>
      </form>
    </ModalComponent>
  </div>
</template>

<style scoped>
.register-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
.register-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 86%;
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
  margin: 5px 0;
}
.register-title {
  font-size: 18px;
}
.login-button {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 94%;
  height: 12%;
  background-color: #9167cc;
  border-color: transparent;
  color: #ffffff;
  font-size: 12px;
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.1s;
  text-decoration: none;
}
.login-button:active {
  background-color: #805bb5;
}
</style>
