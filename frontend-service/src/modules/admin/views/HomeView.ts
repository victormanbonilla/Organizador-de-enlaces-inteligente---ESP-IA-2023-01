import { inject, onMounted, ref, defineComponent } from 'vue';
import { ElMessage } from 'element-plus';
import { useForm } from 'vee-validate';

import TableComponent from '../components/TableComponent.vue';
import AppInputArray from '../components/AppInputArray.vue';
import AppSpinner from '../components/AppSpinner.vue';
import AppModal from '../components/AppModal.vue';

import { useConsults } from '../composables/useConsults';
import { keyFormState } from '../utils/formKey';
import { Table } from '../interfaces/consult';

interface ConsultForm {
  consults: Array<string>;
}

export default defineComponent({
  name: 'HomeView',
  components: {
    TableComponent,
    AppInputArray,
    AppSpinner,
    AppModal,
  },
  setup: () => {
    const data = ref<Table[]>();
    const [formState, setFormState] = inject(keyFormState)!;
    const spinnerState = ref(false);

    const { getConsults, saveConsults, deleteTable } = useConsults();
    const { handleSubmit } = useForm<ConsultForm>({
      initialValues: {
        consults: [''],
      },
    });

    const success = () => {
      ElMessage({
        showClose: true,
        message: 'Success',
        type: 'success',
      });
    };

    const getData = async () => {
      data.value = await getConsults();
    };

    const addHttps = (urls: string[]) => {
      const regex = /^https:\/\//;
      const cleanUrls = [];

      for (const url of urls) {
        regex.test(url)
          ? cleanUrls.push(url)
          : cleanUrls.push(url.replace(/^http:\/\//, 'https://'));
      }

      return cleanUrls;
    };

    const onSubmit = handleSubmit(async ({ consults }, { resetForm }) => {
      const resp = await saveConsults(addHttps(consults), spinnerState);
      resetForm();
      if (resp) {
        success();
        setFormState();
        await getData();
      }
    });

    onMounted(async () => {
      await getData();
    });

    return {
      // Methods
      setFormState,
      deleteTable,
      onSubmit,

      // Properties
      spinnerState,
      formState,
      data,

      // Componentes
      TableComponent,
      AppInputArray,
      AppSpinner,
      AppModal,
    };
  },
});
