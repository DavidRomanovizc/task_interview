from typing import Any, Callable


def strict[T: Callable[..., Any]](func: T) -> T:
    def check_type(
            arg_name: str,
            arg_value: Any,
            annotations: dict[str, type]
    ) -> None:
        if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
            raise TypeError(
                f"Argument '{arg_name}' must be of type {annotations[arg_name].__name__}, but got {type(arg_value).__name__}")

    def inner(*args: Any, **kwargs: Any) -> Any:
        annotations: dict[str, type] = func.__annotations__

        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            check_type(arg_name, arg_value, annotations)

        for arg_name, arg_value in kwargs.items():
            check_type(arg_name, arg_value, annotations)
        return func(*args, **kwargs)

    return inner
