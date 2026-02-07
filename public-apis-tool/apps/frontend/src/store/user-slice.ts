import type { User } from "@repo/shared";

export interface UserStore {
  user: User | null;
  setUser: (user: User) => void;
  clearUser: () => void;
}

export const createUserSlice = (set: any): UserStore => ({
  user: null,
  setUser: (user) => set({ user }),
  clearUser: () => set(null),
});
