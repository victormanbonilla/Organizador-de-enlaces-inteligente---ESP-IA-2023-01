import { Ref, ref } from 'vue';
import { http } from '../../../environments/environment.prod';
import { useAuthStore } from '../../auth/composables/useAuthStore';
import { HomeGetConsultsResponse, PostConsultsReponse } from '../interfaces/consult';

function useConsults() {
  const baseUrl = '/lists';
  const { user } = useAuthStore();
  const rawUser = { ...user.value };

  const getConsults = async() => {
    const url = `${baseUrl}/get_lists/${rawUser.name}`;

    try {
      const { data } = await http.get<HomeGetConsultsResponse>(url);
      return data.data;
    } catch (error) {
      console.log({ error });
    }
  }

  const saveConsults =  async (urls: string[], isLoading: Ref<boolean>) => {
    const response = ref(false);
    
    try {
      // Post request to model
      const urlPredicTable = `model/predict_table`;
      const bodyPredicTable = { urls };
      isLoading.value = true;
      
      const { data } = await http.post<PostConsultsReponse>(urlPredicTable, bodyPredicTable);
      
      // Post request for save the model
      const urlSaveList = `${baseUrl}/save_list`;
      const body = { user: rawUser.name, data: data.data };
      await http.post<{ success: boolean }>(urlSaveList, body)

      response.value = true;
      isLoading.value = false;
    } catch (error) {
      console.log({ error });
    }
    return { response };
  }

  const deleteTable = async (id: string) => {
    const url = `${baseUrl}/delete/${id}`;
    
    try {
      await http.delete(url);
      return true;
    } catch (error) {
      console.error({ error });
      return false;
    }
  }

  return { getConsults, saveConsults, deleteTable };
}

export { useConsults };
