<script lang="ts" src="./HomeView" />

<template>
  <div class="home-container">
    <div
      v-for="(datum, index) in data"
      :key="datum.created_at"
      class="table-container"
    >
      <TableComponent
        :consults="datum.data"
        :date="datum.created_at"
        :index="index"
        :code="datum.code"
        @delete="($emit) => onDelete($emit)"
        @active-modal="
          ($emit) => {
            sharedText = $emit;
            activeModalShare = true;
          }
        "
      />
    </div>
    <AppModal :active="formState">
      <form
        class="form-consults"
        @submit.prevent="onSubmit"
      >
        <div class="title-container">
          <h1 class="form-consults-title">
            Consults Form
          </h1>
          <AppInputArray
            id="arr-urls"
            :meta="meta"
            arr-name="consults"
            placeholder="https://url.com"
            title="Url"
          />
        </div>

        <div class="btn-utils">
          <button
            class="btn-save"
            type="submit"
            :disabled="!meta.valid"
          >
            Save
          </button>
          <button
            class="btn-cancel"
            type="button"
            @click="onClose"
          >
            Cancel
          </button>
        </div>
      </form>
    </AppModal>
    <AppSpinner :active="spinnerState" />

    <el-dialog
      v-model="activeModalShare"
      title="Share"
      width="30%"
      destroy-on-close
      center
      align-center
    >
      <div class="shared-content-container">
        <span class="shared-text">{{ sharedText.slice(0, 24) + ' ...' }}</span>
        <button
          class="btn-copy"
          @click="shareTable"
        >
          Copy
        </button>
      </div>
    </el-dialog>
  </div>
</template>

<style scoped>
.home-container {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  overflow-y: auto;
}
.table-container {
  height: auto;
  width: 98%;
  padding: 10px 10px;
  margin: 10px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  background-color: white;
  border-radius: 20px;
  margin-top: 20px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px,
    rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
}
.form-consults {
  width: 80%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 20px 0;
  flex: 1;
}
.form-consults-title {
  font-size: 22px;
  padding: 12px 0;
}
.btn-utils {
  width: 100%;
  padding-top: 10px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}
.title-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}
.btn-save {
  border-color: transparent;
  background-color: #9c3979;
  color: white;
  padding: 2px 38px;
  border-radius: 10px;
  cursor: pointer;
}
.btn-save:active {
  background-color: #7d2d61;
}
.btn-save:disabled {
  cursor: default;
  background-color: #63244d;
}
.btn-cancel {
  border-color: #9c3979;
  background-color: white;
  color: #9c3979;
  padding: 2px 30px;
  border-radius: 10px;
  cursor: pointer;
}
.btn-cancel:active {
  background-color: #cfcccc;
}

.shared-text {
  background-color: #d4d2d2;
  padding: 10px;
  border-color: transparent;
  border-radius: 12px;
}

.shared-content-container {
  height: fit-content;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}

.btn-copy {
  background-color: #598bff;
  color: white;
  padding: 2px 10px;
  border-color: transparent;
  border-radius: 6px;
  cursor: pointer;
}
.btn-copy:active {
  background-color: #456bc4;
}
</style>
