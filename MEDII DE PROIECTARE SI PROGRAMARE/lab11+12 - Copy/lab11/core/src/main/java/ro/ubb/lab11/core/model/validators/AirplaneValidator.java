package ro.ubb.lab11.core.model.validators;


import org.springframework.stereotype.Component;
import ro.ubb.lab11.core.exceptions.ValidatorException;
import ro.ubb.lab11.core.model.Airplane;

import java.util.stream.Stream;

@Component
public class AirplaneValidator implements Validator<Airplane>{
    @Override
    public void validate(Airplane Airplane) throws ValidatorException {
        /*Stream.of(new Pair<>(Airplane.getName().isEmpty(), "Airplane name must not be empty"),
                        new Pair<>(Airplane.getAge()< 0, "Age must be a positive number"),
                        new Pair<>(Airplane.getPet().isEmpty(), "Pet must not pe empty"))
                .filter(Pair::getLeft)
                .forEach((b) -> {
                    throw new ValidatorException(b.getRight());
                });*/
    }
}
