import { create } from "zustand";
import { createUserSlice, type UserStore } from "./user-slice";

export type Store = UserStore;

export const useStore = create<Store>()((set) => ({
  ...createUserSlice(set),
}));
