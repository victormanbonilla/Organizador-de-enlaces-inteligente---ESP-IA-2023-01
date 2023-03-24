import { inject, onMounted, ref, defineComponent, markRaw } from 'vue';
import { ElMessage } from 'element-plus';
import { useForm } from 'vee-validate';

import TableComponent from '../components/TableComponent.vue';
import AppInputArray from '../components/AppInputArray.vue';
import AppSpinner from '../components/AppSpinner.vue';
import AppModal from '../components/AppModal.vue';

import { useConsults } from '../composables/useConsults';
import { keyFormState } from '../utils/formKey';
import { Table } from '../interfaces/consult';
import { object, string, array } from 'yup';

interface ConsultForm {
  consults: Array<{ url: string; id: number }>;
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

    const urlRegex =
      /((https?):\/\/)?(www.)?[a-z0-9]+(\.[a-z]{2,}){1,3}(#?\/?[a-zA-Z0-9#]+)*\/?(\?[a-zA-Z0-9-_]+=[a-zA-Z0-9-%]+&?)?$/;
    const schema = markRaw(
      object({
        consults: array().of(
          string()
            .matches(urlRegex, 'Enter a valid url')
            .required('Please enter a value')
        ),
      })
    );

    const { getConsults, saveConsults, deleteTable } = useConsults();
    const { handleSubmit, resetForm } = useForm<ConsultForm>({
      initialValues: {
        consults: [{ url: '', id: 0 }],
      },
      validationSchema: schema,
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

    const onSubmit = handleSubmit(async ({ consults }, { resetForm }) => {
      const data = consults.map(consult => (consult.url));
      const resp = await saveConsults(data, spinnerState);
      resetForm();
      if (resp) {
        success();
        setFormState();
        await getData();
      }
    });

    const onClose = () => {
      setFormState();
      resetForm({
        values: {
          consults: [{ url: '', id: 0 }],
        },
      });
    };

    const onDelete = async (code: string) => {
      const resp = await deleteTable(code);
      if (resp) {
        success();
        getData();
      }
    };

    onMounted(async () => {
      await getData();
    });

    return {
      // Methods
      setFormState,
      deleteTable,
      onSubmit,
      onDelete,
      onClose,

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
