import { apiClient } from "@/api/api-client";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Switch } from "@/components/ui/switch";
import { ADD_API_ROUTE, GET_CATEGORIES } from "@/utils/constants";
import type { ApiType } from "@repo/shared";
import React, { useEffect, useState } from "react";
import { BeatLoader } from "react-spinners";
import { AuthEnum, CORSEnum } from "@repo/shared";
import { toast } from "sonner";

const PRForm = () => {
  const [category, setCategory] = useState("");
  const [name, setName] = useState("");
  const [link, setLink] = useState("");
  const [description, setDescription] = useState("");
  const [auth, setAuth] = useState("No");
  const [https, setHttps] = useState(false);
  const [cors, setCors] = useState("Unknown");

  const [creating, setCreating] = useState(false);

  const authValues = ["No", "OAuth", "apiKey", "X-Mashape-Key", "User-Agent"];
  const corsValues = ["Unknown", "No", "Yes"];
  const [categories, setCategories] = useState([]);

  function parseAuthEnum(value: string): AuthEnum {
    switch (value) {
      case "OAuth":
        return AuthEnum.OAuth;
      case "apiKey":
        return AuthEnum.apiKey;
      case "X-Mashape-Key":
        return AuthEnum.XMashapeKey;
      case "No":
        return AuthEnum.No;
      case "User-Agent":
        return AuthEnum.UserAgent;
      default:
        return AuthEnum.No;
    }
  }

  function parseCORSEnum(value: string): CORSEnum {
    if (Object.values(CORSEnum).includes(value as CORSEnum)) {
      return value as CORSEnum;
    }
    return CORSEnum.Unknown;
  }

  const getCategories = async () => {
    await apiClient
      .get(GET_CATEGORIES, { withCredentials: true })
      .then((res) => {
        setCategories(res.data.categories);
        setCategory(res.data.categories[0]);
      });
  };

  useEffect(() => {
    getCategories();
  }, []);

  const hasForbiddenChars = (text: string): boolean => {
    return /[\\[\]|]/.test(text);
  };

  const canSubmit = (): boolean => {
    if (hasForbiddenChars(name)) {
      toast.error("Name has forbidden characters (|, [, ])");
    }
    if (hasForbiddenChars(link)) {
      toast.error("Link has forbidden characters (|, [, ])");
    }
    if (hasForbiddenChars(description)) {
      toast.error("Description has forbidden characters (|, [, ])");
    }

    return true;
  };

  const resetFields = () => {
    setCategory(categories[0]);
    setName("");
    setLink("");
    setDescription("");
    setAuth("No");
    setHttps(false);
    setCors("Unknown");
  };

  const handleSubmit = async () => {
    if (!canSubmit()) {
      return;
    }

    setCreating(true);

    const api: ApiType = {
      name: name,
      category,
      link,
      description,
      auth: parseAuthEnum(auth),
      https,
      cors: parseCORSEnum(cors),
    };

    try {
      const res = await toast.promise(
        () => apiClient.post(ADD_API_ROUTE, api, { withCredentials: true }),
        {
          loading: "Creating Pull Request...",
          success: () => "Pull Request was created successfully",
          error: () => "Error in creating Pull Request",
        },
      );

      console.log((await res.unwrap()).data);
      resetFields();
    } catch (err) {
      console.error(err);
    } finally {
      setCreating(false);
    }
  };

  if (!categories || categories.length == 0)
    return (
      <div className="flex w-full items-center justify-center px-2">
        <BeatLoader color="#1d4ed8" size={18} />
      </div>
    );

  return (
    <div className="flex w-full items-center justify-center px-2">
      <div className="flex flex-col w-full gap-3 max-w-132">
        <div className="flex flex-col">
          <label className="opacity-75 px-2">Category</label>
          <Select
            defaultValue={categories[0]}
            value={category}
            onValueChange={(val) => {
              setCategory(val);
            }}
          >
            <SelectTrigger className="w-full outline-0 border-0 bg-zinc-800 text-md p-2">
              <SelectValue />
            </SelectTrigger>
            <SelectContent position="popper">
              <div className="max-h-[60vh]">
                {categories.map((val) => (
                  <SelectItem key={val} value={val}>
                    {val}
                  </SelectItem>
                ))}
              </div>
            </SelectContent>
          </Select>
        </div>
        <div className="flex flex-col">
          <label htmlFor="name" className="opacity-75 px-2">
            API Name
          </label>
          <input
            name="name"
            id="name"
            type="text"
            className="bg-zinc-100 dark:bg-zinc-800 rounded-md p-2 outline-0"
            value={name}
            onChange={(e) => {
              setName(e.target.value);
            }}
          />
        </div>
        <div className="flex flex-col">
          <label htmlFor="link" className="opacity-75 px-2">
            API Link
          </label>
          <input
            name="link"
            id="link"
            type="text"
            className="bg-zinc-100 dark:bg-zinc-800 rounded-md p-2 outline-0"
            value={link}
            onChange={(e) => {
              setLink(e.target.value);
            }}
          />
        </div>
        <div className="flex flex-col">
          <label htmlFor="description" className="opacity-75 px-2">
            Description
          </label>
          <textarea
            maxLength={100}
            name="description"
            id="description"
            className="bg-zinc-100 dark:bg-zinc-800 rounded-md p-2 outline-0 resize-none"
            value={description}
            onChange={(e) => {
              setDescription(e.target.value);
            }}
          ></textarea>
        </div>
        <div className="flex flex-col">
          <label className="opacity-75 px-2">Auth</label>
          <Select
            defaultValue={authValues[0]}
            value={auth}
            onValueChange={(val) => {
              setAuth(val);
            }}
          >
            <SelectTrigger className="w-full outline-0 border-0 bg-zinc-800 text-md p-2">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              {authValues.map((val) => (
                <SelectItem key={val} value={val}>
                  {val}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div className="flex flex-col gap-2 px-2">
          <label className="opacity-75">HTTPS</label>
          <Switch checked={https} onCheckedChange={setHttps} />
        </div>

        <div className="flex flex-col">
          <label className="opacity-75 px-2">CORS</label>
          <Select
            defaultValue={corsValues[0]}
            value={cors}
            onValueChange={(val) => {
              setCors(val);
            }}
          >
            <SelectTrigger className="w-full outline-0 border-0 bg-zinc-800 text-md p-2">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              {corsValues.map((val) => (
                <SelectItem key={val} value={val}>
                  {val}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <button
          disabled={!name || !link || !description || creating}
          className="bg-blue-700 text-zinc-100 mt-2 w-full text-center p-2 shadow-blue-700/30 hover:bg-blue-600 hover:shadow-lg disabled:hover:shadow-none disabled:bg-blue-950 disabled:cursor-auto rounded-lg cursor-pointer transition-all duration-300"
          onClick={handleSubmit}
        >
          {creating ? "Adding API..." : "Add API"}
        </button>
      </div>
    </div>
  );
};

export default PRForm;
